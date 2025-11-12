from aiogram.filters import Filter
from aiogram.types import Message


class EditCommand(Filter):
    async def __call__(self, message: Message):
        return message.text in ('/edit_name', '/edit_lvl', '/edit_mode')
