from aiogram import Dispatcher, Bot, types
from settings import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage



bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
