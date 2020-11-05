import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'oc#!p70)#rz26!1s^c9))y3$%&wlr=d!ay-t9qgrwk^@_bga8y'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    }
}

DEBAG = True