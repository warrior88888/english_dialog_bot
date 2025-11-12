import logging

from aiogram import Router, F
from aiogram.types import Message

from app.bot.utils import add_new_message
from app.infrastructure.database import Repositories
from app.infrastructure.models import UserOrm
from app.infrastructure.models.enums import ModeChecksEnum, RolesEnum
from app.infrastructure.models.schemas import lexicon
from app.services.chatgpt.chatgpt import chatgpt

dilog_router = Router()
logger = logging.getLogger()


@dilog_router.message(F.text)
async def english_dialog(
        message: Message, user: UserOrm, repo: Repositories
) -> None:
    """
    Base function for dialog
    :param message:
    :param user:
    :param repo:
    :return:
    """
    think_msg = await message.answer(lexicon.handlers.thinking)
    new_dialog = add_new_message(msg_role=RolesEnum.user.name,
                                  messages=str(user.dialog),
                                  message_text=message.text)
    user.dialog = new_dialog
    user.before_feedback -= 1

    if user.before_feedback == 0:
        response = await chatgpt.give_feedback(user)
        user.before_feedback = getattr(ModeChecksEnum, user.mode.name)
        user.last_feedback = response

    else:
        response = await chatgpt.answer_user(user)
        user.dialog = add_new_message(msg_role=RolesEnum.ai.name,
                                     messages=str(user.dialog),
                                     message_text=response)

    await think_msg.delete()
    await message.answer(response)