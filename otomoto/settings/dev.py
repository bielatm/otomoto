from otomoto.settings.settings import *

DATABASES['default'].update(
    {
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'PORT': '5432',
        'HOST': 'localhost',
    }
)