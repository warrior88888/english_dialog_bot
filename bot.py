import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram_dialog import setup_dialogs

from app.infrastructure.cache import redis_cli
from app.infrastructure.database.engine import crete_tables
from config.config import settings

from app.bot.handlers import user_commands, dilog_router, incorrect_type
from app.bot.dialogs import registration_dialog
from app.bot.middlewares import setup_middlewares
from app.bot.commands import set_default_commands

logging.basicConfig(
    level=settings.log.LEVEL,
    format=settings.log.FORMAT,
)


async def main():
    await crete_tables()
    await redis_cli.test()

    storage = RedisStorage(
        redis=redis_cli.redis,
        key_builder=DefaultKeyBuilder(with_destiny=True),
        data_ttl=settings.redis.TTL
    )

    bot = Bot(
        token=settings.telegram.TOKEN.get_secret_value(),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    )

    dp = Dispatcher(storage=storage)
    dp.include_routers(
        registration_dialog, user_commands,
        dilog_router, incorrect_type
    )

    setup_dialogs(dp)
    setup_middlewares(dp=dp, user_router=dilog_router)

    await set_default_commands(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
