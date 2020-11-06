import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'oc#!p70)#rz26!1s^c9))y3$%&wlr=d!ay-t9qgrwk^@_bga8y'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True