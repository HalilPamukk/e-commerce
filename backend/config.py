import os 
from environs import Env

env = Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env.read_env(os.path.join(BASE_DIR, '.env'))


############# ############### ############# ############### ############# ############### ############# ###############

# SECURITY WARNING: keep the secret key used in production secret! 
SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=True)

# Redis settings
REDIS_BACKEND = os.getenv("REDIS_BACKEND", "django_redis.cache.RedisCache")
REDIS_SERVER = os.getenv("REDIS_SERVER")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_DB = os.getenv("REDIS_DB", 0)
REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", 1)
REDIS_CACHE_DB = os.getenv("REDIS_CACHE_DB", 2)
REDIS_CONSTANCE_DB = os.getenv("REDIS_CONSTANCE_DB", 3)
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_CONNECT_TIMEOUT = os.getenv("REDIS_CONNECT_TIMEOUT", 5)
REDIS_SOCKET_TIMEOUT = os.getenv("SOCKET_TIMEOUT", 5)

# Session settings
SESSION_ENGINE = os.getenv("SESSION_ENGINE", "django.contrib.sessions.backends.db")
SESSION_CACHE_ALIAS = os.getenv("SESSION_CACHE_ALIAS", "default")
SESSION_COOKIE_SECURE = True

# SMTP-EMAIL settings
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", True)
EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.getenv("EMAIL_PORT")

# CELERY SETTINGS
CELERY_BROKER_URL = f'redis://{REDIS_SERVER}:{REDIS_PORT}/{REDIS_CELERY_DB}'
CELERY_RESULT_BACKEND =  f'redis://{REDIS_SERVER}:{REDIS_PORT}/{REDIS_CELERY_DB}'

# DATABASE SETTINGS
POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

# replica
REPLICA_POSTGRES_SERVER = os.getenv("REPLICA_POSTGRES_SERVER", POSTGRES_SERVER)
REPLICA_POSTGRES_USER = os.getenv("REPLICA_POSTGRES_USER", POSTGRES_USER)
REPLICA_POSTGRES_PASSWORD = os.getenv("REPLICA_POSTGRES_PASSWORD", POSTGRES_PASSWORD)
REPLICA_POSTGRES_DB = os.getenv("REPLICA_POSTGRES_DB", POSTGRES_DB)
REPLICA_POSTGRES_PORT = os.getenv("REPLICA_POSTGRES_PORT", POSTGRES_PORT)

# Logging settings
SHOW_DJANGO_LOG = os.getenv("SHOW_DJANGO_LOG", True)
LOGGING_LOG_LEVEL = os.getenv("LOGGING_LOG_LEVEL", "INFO")

# SENTRY settings
SENTRY_DSN = os.getenv("SENTRY_DSN")
SENTRY_ENVIRONMENT = os.getenv("SENTRY_ENVIRONMENT", "development")

# AWS S3 settings
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_S3_REGION = os.getenv("AWS_S3_REGION")
AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")
IMAGE_URL = os.getenv("IMAGE_URL")