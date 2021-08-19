from .base import *

DEBUG = False

ALLOWED_HOSTS = ['lk.praesens.ru', 'localhost', 'spnavigator.ru',]
CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'NAME': 'lk',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'dev',
        'PASSWORD': 'dev',
        'HOST': '127.0.0.1',
        'PORT': 5432,
        'CONN_MAX_AGE': 300
    }
}

SITE_ID = 1
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#         'json': {
#             'format': '{ "loggerName":"%(name)s", "timestamp":"%(asctime)s", "fileName":"%(filename)s", "logRecordCreationTime":"%(created)f", '
#                       '"functionName":"%(funcName)s", "levelNo":"%(levelno)s", "lineNo":"%(lineno)d", "time":"%(msecs)d", "levelName":"%(levelname)s", "message":"%(message)s"}',
#         },
#     },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose',
#         },
#         'sql.file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': ROOT_DIR / 'log' / 'sql.log',
#         },
#         'debug.file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': ROOT_DIR / 'log' / 'debug.log',
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'level': 'DEBUG',
#             # 'handlers': ['console'],
#             'handlers': ['sql.file', ],
#         },
#         'default': {
#             'level': 'DEBUG',
#             'handlers': ['console', 'debug.file']
#         },
#     }
# }

INTERNAL_IPS = [
    '127.0.0.1',
]

# TODO изучить вопрос
# SENTRY.IO интеграция

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://4679c94562204703b503b40de30aa5af@o118467.ingest.sentry.io/5864319",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)