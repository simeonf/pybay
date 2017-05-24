import os
from pybay.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
EMAIL_DEBUG = DEBUG

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        'OPTIONS': {
            'read_default_file': '/home/pybay/pybay_prod.cnf',
        },
    }
}

ALLOWED_HOSTS = ['prod.pyconsf.com', 'pyconsf.com', 'www.pyconsf.com', 'www.pybay.com', 'pybay.com', 'prod.pybay.com']

TIME_ZONE = "US/Pacific"

MEDIA_ROOT = '/data/websites/prod_site_media/media'
MEDIA_URL = "/site_media/media/"

STATIC_ROOT = '/data/websites/prod_site_media/static'
STATIC_URL = "/site_media/static/"

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
