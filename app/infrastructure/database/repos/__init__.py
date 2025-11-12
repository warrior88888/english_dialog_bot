from __future__ import annotations

from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession

from .user import UserRepo


@dataclass
class Repositories:
    session: AsyncSession
    user: UserRepo

    @staticmethod
    def get_repo(session: AsyncSession) -> Repositories:
        return Repositories(session=session, user=UserRepo(session))


__all__ = [
    "Repositories",
]
