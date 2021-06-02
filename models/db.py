import asyncio
import asyncpg

from pprint import pprint 

from settings import *

import os
from os import listdir

async def create_pool():
    return await asyncpg.create_pool(user=DB_USERNAME, password=DB_PASSWORD, database=DB_NAME, host=DB_HOST)


loop = asyncio.get_event_loop()
db = loop.run_until_complete(create_pool())


class DBCommands:
    pool = db
    #Сделать пуул более самостоятельным, не зависимым от единого объекта
    
    async def migrate_all_models(self):
        commands = []
        print(listdir(BASE_DIR+'/models/sql/'))
        for file in listdir(BASE_DIR+"/models/sql/"):        
            command = open(BASE_DIR+"/models/sql/"+file).read()
            pprint(command)
            commands.append(command)
        for command in commands: 

            try:
                await self.pool.fetchval(command)
                print('ok')
            except Exception as e:
                print(e)
                