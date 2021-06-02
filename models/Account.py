from .db import create_pool
import asyncio
from log import log

class Account():
    def __init__(self, db, id, name, age, text, *args, **kwargs):
        loop = asyncio.get_event_loop()
        self.id = id
        self.name = name
        self.age = age
        self.text = text
        self.db = db
        #self.is_human = is_human
        


    async def save(self, **kwargs):
        command = f"insert into Account(id, name, age, text) values ({self.id}, '{self.name}', {self.age}, '{self.text}');"
        print(command)
        try:
            await self.db.fetchval(command)
            #log.info(f'Account {self.name} - {self.age} - {self.text} - {self.is_human} - {self.id} CREATED')
            log.info(f'Account {self.name} - {self.age} - {self.text} - {self.id} CREATED')
        except Exception as e:
            print(e)
            log.error(f'Account {self.name} - {self.age} - {self.text} - {self.id} NOT CREATED')
            #log.error(f'Account {self.name} - {self.age} - {self.text} - {self.is_human} - {self.id} NOT CREATED')

    #ПРОВЕРКА НА НАЛИЧИЕ ПИПИСЬКИ, НЕ ЗАБЫТЬ!!!!