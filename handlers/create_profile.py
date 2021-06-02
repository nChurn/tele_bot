from aiogram import types
from aiogram.dispatcher.filters import Command
from disp import dp

from aiogram.dispatcher import FSMContext
from states.CreateProfileStates import CreateProfileStates

from models.Account import Account
from models.db import db

from log import log

#СДЕЛАТЬ ПРОВЕРКУ НА НАЛИЧИЕ ЧЛЕНА
@dp.message_handler(lambda message: message.text and 'создать анкету' in message.text.lower(),  state=None)
async def create_profile(message: types.Message):
    await message.answer('Напишите имя ')

    await CreateProfileStates.Name.set()


@dp.message_handler(state=CreateProfileStates.Name)
async def set_name(message: types.Message, state: FSMContext):
    answer = message.text
    print(answer)
    await state.update_data(name=answer)

    
    await message.answer('Дурак, укажи свой возраст')
    await CreateProfileStates.next()


@dp.message_handler(state=CreateProfileStates.Age)
async def set_age(message: types.Message, state: FSMContext):
    answer = message.text
    print(answer)
    try:
        answer = int(answer)
    except:
        log.info(f'{message.from_user.id} - {message.from_user.full_name} - set age: {answer}')
        await message.answer('Не правильно указано имя')
    await state.update_data(age=answer)
    await message.answer('Малолетнее чмо, теперь опиши себя')
    await CreateProfileStates.Text.set()
    

@dp.message_handler(state=CreateProfileStates.Text)
async def set_text(message: types.Message, state: FSMContext):
    answer = message.text
    print(answer)
    await state.update_data(text=answer)

    await message.answer('Осталось указать место жительства')
    await CreateProfileStates.Geo.set()

@dp.message_handler(state=CreateProfileStates.Geo)
async def set_geo (message: types.Message, state: FSMContext):
    answer = message.text
    print(answer, 'answer')
    await state.update_data(geo=answer)
    await message.answer('Прекрасно')
    await CreateProfileStates.Check.set()
    print('pososal')

@dp.message_handler(state=CreateProfileStates.Check)
async def check_profile(message: types.Message, state:FSMContext):

    data = await state.get_data()
    print('eshe rabotaet')
    name = data.get('name')
    age = data.get('age')
    text = data.get('text')
    geo = data.get('geo')
    id = message.from_user.id

    await message.answer(f'Давай проверим анкету: \n Имя: {name}\n Возраст: {age}\n Описание:{text}\n Живешь в:{geo}\n Все верно?')
    await CreateProfileStates.End.set()

@dp.message_handler(state=CreateProfileStates.End)
async def save_or_restart(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "Да":
        data = await state.get_data()
        print('eshe rabotaet')
        name = data.get('name')
        age = data.get('age')
        text = data.get('text')
        geo = data.get('geo')
        id = message.from_user.id
    
        acc = Account(db=db, id=id, name=name, age=age, text=text, geo=geo)
        await acc.save()
        await state.finish()

    elif answer == 'Заново':
        await message.answer('Ок, все по новой')
        await CreateProfileStates.Name.set()
    
    else:
        await message.answer('Я не понял ответ, поэтому забудем про анкету')
        await state.finish()