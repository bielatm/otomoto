from otomoto.settings.settings import *

DATABASES['default'].update(
    {
        'NAME': 'otomoto',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
    }
)