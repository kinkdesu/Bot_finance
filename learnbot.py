import os

from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "5202629950:AAEc5X3yMo9I4WZzGSklNVZu3OBWSHUGbxM"

async def main() -> None:
    dp = Dispatcher()
    bot = Bot(os.getenv('token'))
    
