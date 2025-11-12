from aiogram_dialog import DialogManager

from app.infrastructure.models.schemas.lexicon import lexicon


async def format_getter(dialog_manager: DialogManager, **kwargs):
    status = dialog_manager.dialog_data.get('editing', False)
    if not status:
        return {
            'editing': bool(status),
            'choose_name': lexicon.handlers.choose_name,
            'choose_level': lexicon.handlers.choose_level,
            'choose_mode': lexicon.handlers.choose_mode,
            'ready': lexicon.buttons.ready,
        }
    else:
        return {
            'editing': bool(status),
            'choose_name': lexicon.handlers.edit_name,
            'choose_level': lexicon.handlers.edit_lvl,
            'choose_mode': lexicon.handlers.edit_mode,
            'ready': lexicon.buttons.ready,
        }
