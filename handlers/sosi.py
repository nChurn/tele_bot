from aiogram import types
from aiogram.dispatcher.filters import Command
from disp import dp


@dp.message_handler(Command('stas'))
async def sosi(message: types.Message):
    await message.answer('soset') 