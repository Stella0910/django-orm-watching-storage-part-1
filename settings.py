import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('BD_HOST'),
        'PORT': os.getenv('BD_PORT'),
        'NAME': os.getenv('BD_NAME'),
        'USER': os.getenv('BD_USER'),
        'PASSWORD': os.getenv('BD_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('BD_SECRET_KEY')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
