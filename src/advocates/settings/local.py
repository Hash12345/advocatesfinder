import os

from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = os.environ.get('SECRETE_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Base url to serve media files
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'

# Relaxing cors in local
CORS_ALLOW_ALL_ORIGINS = True