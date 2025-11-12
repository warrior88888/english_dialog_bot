from __future__ import annotations

from sqlalchemy import select
from aiogram.types import Message

from app.infrastructure.models.database import UserOrm

from .base import BaseRepo


class UserRepo(BaseRepo):
    model = UserOrm

    async def get_by_tg_id(self, tg_id: int) -> UserOrm | None:
        q = select(self.model).where(self.model.tg_id == tg_id)
        return (await self.session.execute(q)).scalar_one_or_none()
