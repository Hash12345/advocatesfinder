import os
from .base import *

DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('HOST'),
        'NAME': os.environ.get('NAME'),
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'PORT': os.environ.get('PORT'),
    }
}
# Base url to serve media files
STATIC_URL = 'static/'

# Base url to serve media files
MEDUA_URL = '/media/'
MEDUA_ROOT = 'media/'

# Relaxing cors in development
CORS_ALLOW_ALL_ORIGINS = True
