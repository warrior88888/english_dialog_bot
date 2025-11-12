from aiogram import F, Router
from aiogram.types import Message

from app.infrastructure.models.schemas import lexicon

incorrect_type = Router()


@incorrect_type.message(~F.text)
async def non_text_message_handler(message: Message):
    """
    Catch all types after english_dialog
    :param message:
    :return:
    """
    await message.answer(lexicon.handlers.incorrect_input)
