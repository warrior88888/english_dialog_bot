from __future__ import annotations
import logging
from typing import TYPE_CHECKING, Any, Awaitable, Callable

from aiogram import BaseMiddleware, Dispatcher

from app.infrastructure.database.engine import get_repo
from app.infrastructure.models.database import UserOrm

if TYPE_CHECKING:
    from aiogram.types import TelegramObject
    from app.infrastructure.database import Repositories
    from aiogram.types import User as AiogramUser


IGNORED_NAMES = ["Group", "Channel"]

logger = logging.getLogger("DatabaseMiddleware")


class GetRepo(BaseMiddleware):
    """
    Create repo for async db transaction
    """

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        us = data["event_from_user"]

        if us.first_name in IGNORED_NAMES:
            return

        async with get_repo() as repo:
            data["repo"] = repo

            await handler(event, data)


class GetUser(BaseMiddleware):
    """
    Put user to handlers and automatically save all changes
    """

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        repo: Repositories = data["repo"]
        user_: AiogramUser = data["event_from_user"]

        user = await repo.user.get_by_tg_id(user_.id)

        if not user:
            user = UserOrm(tg_id=user_.id)
            logger.info("New user")
            user = await repo.user.update(user)
        data["user"] = user
        await handler(event, data)

        await repo.user.update(user)


def setup_db_middlewares(dp: Dispatcher):
    dp.message.middleware.register(GetRepo())
    dp.callback_query.middleware.register(GetRepo())
    dp.message.middleware.register(GetUser())
    dp.callback_query.middleware.register(GetUser())
