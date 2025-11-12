import logging

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from app.bot.filters import EditCommand
from app.bot.dialogs.registration import User
from app.infrastructure.models import UserOrm
from app.infrastructure.models.schemas.lexicon import lexicon


user_commands = Router()
logger = logging.getLogger(__name__)


@user_commands.message(CommandStart())
async def command_start(
        message: Message, user:UserOrm, dialog_manager: DialogManager
) -> None:
    if not user.name:
        initial_data = {
            'editing': False,
            'level': user.level.value,
            'mode': user.mode.value,
        }
        await message.answer(lexicon.handlers.start)
        await dialog_manager.start(
            User.fill_name,
            mode=StartMode.RESET_STACK,
            data=initial_data
        )
    else:
        await message.answer(lexicon.handlers.start)


@user_commands.message(EditCommand())
async def edit_info(
        message: Message, user: UserOrm, dialog_manager: DialogManager
) -> None:
    field_to_edit = message.text[len("/edit_"):]

    if user.name:
        if field_to_edit == 'name':
            start_state = getattr(User, 'fill_name')
        else:
            start_state = getattr(User, f'choose_{field_to_edit}')
        initial_data = {
            'editing': True,
            'level': user.level.value,
            'mode': user.mode.value,
            'name': user.name,
        }
        await dialog_manager.start(
            state=start_state,
            mode=StartMode.RESET_STACK,
            data=initial_data
        )

    else:
        initial_data = {
            'editing': False,
            'level': user.level.value,
            'mode': user.mode.value,
        }
        await dialog_manager.start(
            User.fill_name,
            mode=StartMode.RESET_STACK,
            data=initial_data
        )


@user_commands.message(Command('reset_dialog'))
async def reset_dialog(message: Message, user: UserOrm) -> None:
    user.dialog = None
    user.last_feedback = None
    await message.answer(lexicon.handlers.reset_dialog)


@user_commands.message(Command('info'))
async def bot_info(message: Message, user: UserOrm) -> None:
    await message.answer(lexicon.handlers.info)
