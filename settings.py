import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('HOST_BD'),
        'PORT': '5434',
        'NAME': os.getenv('NAME_BD'),
        'USER': os.getenv('USER_BD'),
        'PASSWORD': os.getenv('PASSWORD_BD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY_BD')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
