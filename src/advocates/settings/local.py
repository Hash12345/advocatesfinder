from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = 'django-insecure-2+y4*kzi7bg18$8(r(uh4-^*&5mcs%mhai)&sp)=wlpv!&b*eb'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}