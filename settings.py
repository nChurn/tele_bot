from dotenv import dotenv_values
import os, sys
env = dotenv_values()

print(env)

BASE_DIR =  os.path.dirname(__file__)
sys.path.append(BASE_DIR)


BOT_TOKEN = env['BOT_TOKEN']
ADMINS = env['ADMINS']

DB_NAME = env['DB_NAME']
DB_USERNAME = env['DB_USERNAME']
DB_PASSWORD = env['DB_PASSWORD']
DB_HOST = env["DB_HOST"]
DB_PORT = env['DB_PORT']

DB_CONNECTION = f"postgres://{DB_USERNAME}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

DEBUG_MODE = env['DEBUG_MODE']

ALLOWED_HOSTS = [
    'localhost'
]

DATABASES = {
    "default":{
        "ENGINE":'django.db.backends.postgresql',
        "NAME": DB_NAME,
        "USER": DB_USERNAME,
        "PASSWORD": DB_PASSWORD,
        'HOST':DB_HOST,
        "PORT": DB_PORT,
    }
}

DEGUG= bool(DEBUG_MODE)