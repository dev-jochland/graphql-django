from .base import *

from dj_database_url import parse as db_url


if bool(int(config('GITHUB_WORKFLOW'))) is True:  # On github secrets set this as 1, default is 0
    DATABASES = {
        'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'postgres',
           'USER': 'postgres',
           'PASSWORD': 'postgres',
           'HOST': '127.0.0.1',
           'PORT': '5432',
        }
    }
elif bool(int(config('HEROKU_ENV'))) is True:  # on heroku config var, set this as 1, default is 0
    DATABASES = {
        'default': config('DATABASE_URL', cast=db_url),
    }
elif bool(int(config('AWS_ENV'))) is True:  # on aws env set this as 1, default is 0
    DATABASES = {
        'default': {
            'ENGINE': "django.db.backends.postgresql",
            'NAME': config("POSTGRES_DB"),
            'USER': config("POSTGRES_USER"),
            'PASSWORD': config("POSTGRES_PASSWORD"),
            'HOST': config("POSTGRES_HOST"),
            'PORT': 5432,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': "django.db.backends.postgresql",
            'NAME': config("POSTGRES_DB"),
            'USER': config("POSTGRES_USER"),
            'PASSWORD': config("POSTGRES_PASSWORD"),
            'HOST': config("POSTGRES_HOST"),
            'PORT': 5432,
        }
    }
