import logging
from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware, Router
from aiogram.types import TelegramObject

from app.infrastructure.cache import redis_cli
from app.infrastructure.models.schemas import lexicon

logger = logging.getLogger("ThrottlingMiddleware")

class ThrottlingMiddleware(BaseMiddleware):
    """Check if user is not waiting ChatGpt answer"""
    cache = redis_cli.redis

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:

        user = data["event_from_user"]
        user_id = f"throttle:{user.id}"

        if await self.cache.get(user_id):
            await event.answer(lexicon.handlers.stop_spam, show_alert=True)
            logger.info(f"throttle:{user.id} spam")
            return None

        else:
            logger.info(f"{user.id} passed throttle")
            await self.cache.setex(
                user_id, 10, 1
            )
            return await handler(event, data)


def setup_throttling_middleware(user_router: Router):
    user_router.message.middleware.register(ThrottlingMiddleware())
