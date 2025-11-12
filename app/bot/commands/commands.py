from aiogram import Bot
from aiogram.types.bot_command import BotCommand

from lexicon.lexicon import lexicon

commands = [
    BotCommand(command=k, description=v)
    for k, v in lexicon['commands'].items()
]

async def set_default_commands(bot: Bot):
    await bot.set_my_commands(commands)
