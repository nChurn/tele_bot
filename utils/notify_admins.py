from aiogram import Dispatcher



from settings import DB_CONNECTION

async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, 'Bot started')

        except Exception as err:
            print(err)