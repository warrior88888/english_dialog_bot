from datetime import datetime
from pydantic import BaseModel

from app.infrastructure.models.enums import EnglishLvlEnum, ModeLvlEnum


class BaseSchema(BaseModel):
    id: int
    tg_id: int
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        extra = 'ignore'


class UserSchema(BaseSchema):
    name: str | None
    level: EnglishLvlEnum | None
    mode: ModeLvlEnum | None
    current_dialog: int | None
    before_feedback: int | None
    fsm_state: str | None
    is_premium: bool | None


class DialogSchema(BaseSchema):
    num: int
    topic: str | None
    messages = str | None
