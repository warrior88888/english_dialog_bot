import logging

from aiogram import Dispatcher, Router

from .database import setup_db_middlewares
from .throttling import setup_throttling_middleware

def setup_middlewares(dp: Dispatcher, user_router: Router):
    setup_db_middlewares(dp)
    setup_throttling_middleware(user_router)
    logging.info(f'Setup middleware done')
