"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import sys
import os
from . import config
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR + '/apps') # Add apps folder to sys.path


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.SECRET_KEY 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.DEBUG

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'django_filters',
    'drf_yasg', # API documentation
    'corsheaders',
    'django_celery_beat',
    'constance',
    'constance.backends.database',
    'explorer',
    
    # Local apps
    'core', # Core app
    'account', # User management
    'address', # Address management
    'analytics', # Analytics
    'basket', # Basket management
    'catalog', # Product management
    'finance', # Finance management
    'inventory', # Inventory management
    'invoice', # Invoice management
    'notifications', # Notification management
    'orders', # Order management
    'payment', # Payment management
    'promotions', # Discount/voucher management
    'ratings', # Rating management
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config.POSTGRES_DB,
        'USER': config.POSTGRES_USER,
        'PASSWORD': config.POSTGRES_PASSWORD,
        'HOST': config.POSTGRES_SERVER,
        'PORT': config.POSTGRES_PORT,
    },
    'replica': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config.REPLICA_POSTGRES_SERVER,
        'USER': config.REPLICA_POSTGRES_USER,
        'PASSWORD': config.REPLICA_POSTGRES_PASSWORD,
        'HOST': config.REPLICA_POSTGRES_SERVER,
        'PORT': config.REPLICA_POSTGRES_PORT,
    }
}

# Explorer settings
EXPLORER_CONNECTIONS = {"Default": "replica"}
EXPLORER_DEFAULT_CONNECTION = "replica"


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'tr'
TIME_ZONE = "Europe/Istanbul"
USE_I18N = True
#USE_L10N = True
USE_TZ = True

# Localization
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGES = [
    ('en', _('English')),
    ('tr', _('Turkish')),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CONSTANCE settings
CONSTANCE_BACKEND = "constance.backends.redisd.RedisBackend"
CONSTANCE_REDIS_CONNECTION = {
    "host": config.REDIS_SERVER,
    "port": config.REDIS_PORT,
    "db": config.REDIS_CONSTANCE_DB,
    "password": config.REDIS_PASSWORD,
}
from backend.constance_config import *


# CACHE settings
CACHES = {
    "default": {
        "BACKEND": config.REDIS_BACKEND,
        "LOCATION": f"redis://{config.REDIS_SERVER}:{config.REDIS_PORT}/{config.REDIS_CACHE_DB}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": f"{config.REDIS_PASSWORD}",
            "SOCKET_CONNECT_TIMEOUT": int(
                config.REDIS_CONNECT_TIMEOUT
            ),  # in seconds
            "SOCKET_TIMEOUT": int(config.REDIS_SOCKET_TIMEOUT),  # in seconds
        },
    }
}


# CELERY settings
CELERY_BROKER_URL = config.CELERY_BROKER_URL
CELERY_RESULT_BACKEND = config.CELERY_RESULT_BACKEND

# SMTP settings
EMAIL_USE_TLS = config.EMAIL_USE_TLS
EMAIL_BACKEND = config.EMAIL_BACKEND
EMAIL_HOST = config.EMAIL_HOST
EMAIL_HOST_USER = config.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = config.EMAIL_HOST_PASSWORD
EMAIL_PORT = config.EMAIL_PORT

# Logging settings
if config.SHOW_DJANGO_LOG:
    import logging.config

    LOGGING_CONFIG = None

    # Get loglevel from env
    LOGLEVEL = config.LOGGING_LOG_LEVEL

    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "console": {
                    "format": "%(asctime)s %(levelname)s %(message)s",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "console",
                },
            },
            "loggers": {
                "": {
                    "level": LOGLEVEL,
                    "handlers": [
                        "console",
                    ],
                },
            },
        }
    )

# Sentry settings
import sentry_sdk
sentry_sdk.init(
    dsn=config.SENTRY_DSN,
    environment=config.SENTRY_ENVIRONMENT,
)

#AWS S3 settings
AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
AWS_S3_REGION = config.AWS_S3_REGION
AWS_ENDPOINT = f"s3.{AWS_S3_REGION}.amazonaws.com"
AWS_S3_BUCKET_NAME = config.AWS_S3_BUCKET_NAME
AWS_S3_CUSTOM_DOMAIN = f"https://{AWS_S3_BUCKET_NAME}.{AWS_ENDPOINT}"
IMAGE_URL = config.IMAGE_URL