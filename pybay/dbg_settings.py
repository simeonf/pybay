from pybay.settings import *

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE_CLASSES = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE_CLASSES

DEBUG_TOOLBAR = True

INTERNAL_IPS = ['127.0.0.1']
