from typing import Any

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import ManagedRadio, Button

from app.infrastructure.models import UserOrm
from app.infrastructure.models.enums import EnglishLvlEnum, ModeLvlEnum, ModeChecksEnum
from app.infrastructure.models.schemas.lexicon import lexicon


async def on_start(
        start_data: dict,
        dialog_manager: DialogManager,
        **kwargs
) -> None:
    """
    Handler to pre-fill dialog fields when it starts.
    This is useful for the "edit" functionality.
    """
    level_widget: ManagedRadio = dialog_manager.find("level")
    mode_widget: ManagedRadio = dialog_manager.find("mode")

    level_value = start_data.get("level")
    mode_value = start_data.get("mode")

    dialog_manager.dialog_data.update(start_data)

    # Check if values were passed and set the radio buttons
    if level_value:
        await level_widget.set_checked(level_value)
    if mode_value:
        await mode_widget.set_checked(mode_value)


async def error_name(
        message: Message,
        dialog_: Any,
        manager: DialogManager,
        error_: ValueError
):
    """
    Handles incorrect name input (based on validator).
    """
    await message.answer(lexicon.handlers.wrong_name)


async def correct_name(
        message: Message,
        dialog_: Any,
        manager: DialogManager,
        name: str
):
    """
    Handles correct name input.
    Saves the name and moves to the next step or finishes.
    """
    manager.dialog_data['name'] = name
    user: UserOrm = manager.middleware_data.get("user")
    user.name = name

    if manager.dialog_data.get('editing', False):
        await message.answer(lexicon.handlers.edit_done)
        await manager.done()
    else:
        await manager.next()


async def set_level(
        callback: CallbackQuery,
        widget: ManagedRadio,
        manager: DialogManager,
        item_id: str
):
    """
    Handles selection of an English level.
    Saves the level and moves to the next step or finishes.
    """
    manager.dialog_data['level'] = item_id
    user: UserOrm = manager.middleware_data.get("user")
    user.level = getattr(EnglishLvlEnum, item_id)


async def set_mode(
        callback: CallbackQuery,
        widget: ManagedRadio,
        manager: DialogManager,
        item_id: str
):
    """
    Handles selection of a mode.
    Saves the mode and finishes the dialog.
    """
    manager.dialog_data['mode'] = item_id
    user: UserOrm = manager.middleware_data.get("user")
    user.mode = getattr(ModeLvlEnum, item_id)
    user.before_feedback = getattr(ModeChecksEnum, item_id)


async def set_level_ready(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    if manager.dialog_data.get('editing', False):
        await callback.message.answer(lexicon.handlers.edit_done)
        await manager.done()
    else:
        await manager.next()


async def set_mode_ready(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    if manager.dialog_data.get('editing', False):
        await callback.message.answer(lexicon.handlers.edit_done)
        await manager.done()
    else:
        await callback.message.answer(lexicon.handlers.completed)
        await manager.done()
