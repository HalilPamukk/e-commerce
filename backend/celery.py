from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from kombu import Exchange, Queue
from .config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app = Celery("backend", broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

default_exchange = Exchange("default", type="direct")

app.conf.task_queues = (
    # for example ---> Queue("create-log", default_exchange, routing_key="create-log"),
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
