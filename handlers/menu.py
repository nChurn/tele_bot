from disp import dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from keyboards.default import menu

@dp.message_handler(Command('menu'))
async def show_menu(msg: Message):
    print('as')
    await msg.answer('mark',reply_markup=menu)
