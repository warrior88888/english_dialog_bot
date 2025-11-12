from sqlalchemy import Boolean, Enum, Integer, String, text
from sqlalchemy.orm import mapped_column, Mapped

from app.infrastructure.models.enums import EnglishLvlEnum, ModeLvlEnum

from .base import BaseOrm


class UserOrm(BaseOrm):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(24), nullable=True)
    level: Mapped[EnglishLvlEnum] = mapped_column(
       Enum(EnglishLvlEnum), server_default=EnglishLvlEnum.a2
    )
    mode: Mapped[ModeLvlEnum] = mapped_column(
        Enum(ModeLvlEnum), server_default=ModeLvlEnum.normal
    )
    dialog: Mapped[str | None] = mapped_column(String, nullable=True)
    last_feedback: Mapped[str | None] = mapped_column(String, nullable=True)
    before_feedback: Mapped[int | None] = mapped_column(
        Integer,
        nullable=False,
        server_default=text("5")
    )
    fsm_state: Mapped[str | None] = mapped_column(String(32), nullable=True)
    is_premium: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default=text("false")
    )
