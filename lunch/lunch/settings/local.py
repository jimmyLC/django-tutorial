from .base import *

SECRET_KEY = '(olor5-akq)1kjaiql=z)pg_f!4t)tq^^-k=8)=c$2d5*k&*sw'
DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}