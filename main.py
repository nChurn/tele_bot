from aiogram import executor
from disp import dp

import handlers

#from utils.set_default_commands import set_default_commands
#from utils.notify_admins import on_startup_notify

import asyncio
from models.db import DBCommands
from pprint import pprint

#async def on_startup(dp):
#    await set_default_commands(dp)

#    await on_startup_notify(dp)

from settings import *

if __name__ == '__main__':
    db_commands = DBCommands()
    
    loop = asyncio.get_event_loop()
    
    loop.run_until_complete(db_commands.migrate_all_models())
    print('loop started')
    executor.start_polling(dp)
