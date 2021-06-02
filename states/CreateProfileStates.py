from aiogram.dispatcher.filters.state import StatesGroup, State

class CreateProfileStates(StatesGroup):
    Name = State()
    Age = State()
    Text = State()
    Geo = State()
    Check = State()
    End = State()