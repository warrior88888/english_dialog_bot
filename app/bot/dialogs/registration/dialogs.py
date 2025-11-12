import logging
import operator

from aiogram_dialog import Dialog
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Radio, Button
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.input import TextInput

from app.infrastructure.models.enums import EnglishLvlEnum, ModeLvlEnum
from .getters import format_getter
from .handlers import (
    correct_name, error_name, set_mode, set_level,
    on_start, set_level_ready, set_mode_ready
)
from .states import User
from .validators import type_factory_english_name, enum_to_list

logger = logging.getLogger(__name__)

registration_dialog = Dialog(
    Window(
        Format("{choose_name}"),
        TextInput(
            id="name",
            on_error=error_name,
            on_success=correct_name,
            type_factory=type_factory_english_name,
        ),
        state=User.fill_name,
    ),
    Window(
        Format("{choose_level}"),
        Group(
            Radio(
                Format("✅ {item[0]}"),
                Format("{item[0]}"),
                id="level",
                item_id_getter=operator.itemgetter(1),
                items=enum_to_list(EnglishLvlEnum),
                on_click=set_level,
            ),
            width=3
        ),
        Button(
            Format("{ready}"),
            id="ready",
            on_click=set_level_ready,
        ),
        state=User.choose_lvl,
    ),
    Window(
        Format("{choose_mode}"),
        Group(
            Radio(
                Format("✅ {item[0]}"),
                Format("{item[0]}"),
                id="mode",
                item_id_getter=operator.itemgetter(1),
                items=enum_to_list(ModeLvlEnum),
                on_click=set_mode,
            ),
            width=1
        ),
        Button(
            Format("{ready}"),
            id="ready",
            on_click=set_mode_ready,
        ),
        state=User.choose_mode,
    ),
    getter=format_getter,
    on_start=on_start
)
