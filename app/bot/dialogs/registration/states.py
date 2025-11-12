from aiogram.filters.state import StatesGroup, State

class User(StatesGroup):
    fill_name = State()
    choose_lvl = State()
    choose_mode = State()
