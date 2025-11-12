from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING, Any, TypeVar

from sqlalchemy import select

from app.infrastructure.models.database import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


Model = TypeVar("Model", bound=Base)


class BaseRepo(ABC):
    model: Base

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

        if self.model is None:
            msg = "model is not set"
            raise NotImplementedError(msg)

    async def create(self, **kwargs: dict[str, Any]) -> Model:
        db_obj: Model = self.model(**kwargs)
        return await self.create_from_model(db_obj)

    async def create_from_model(self, *db_obj: Model) -> Model | tuple[Model]:
        for i in db_obj:
            self.session.add(i)
        await self.session.commit()

        return db_obj[0] if len(db_obj) == 1 else db_obj

    async def get(self, db_object_id: int) -> Model | None:
        q = select(self.model).where(self.model.id == db_object_id)
        return (await self.session.execute(q)).scalar_one_or_none()

    async def delete(self, *db_objects: Model) -> None:
        for i in db_objects:
            await self.session.delete(i)
        await self.session.commit()

    async def update(self, db_object: Model) -> Model:
        merged = await self.session.merge(db_object)
        await self.session.commit()
        await self.session.refresh(merged)
        return merged
