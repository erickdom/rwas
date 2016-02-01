from __future__ import absolute_import

from datetime import timedelta

BROKER_URL = 'amqp://usrrwas:rwas2016%@localhost:5672/vhostrwas'
CELERY_RESULT_BACKEND = 'amqp://usrrwas:rwas2016%@localhost:5672/vhostrwas'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True


CELERYBEAT_SCHEDULE = {
    'sender': {
        'task': 'requests.tasks.ReceiverTask',
        'schedule': timedelta(seconds=5),
    },
    'receiver': {
        'task': 'requests.tasks.SenderTask',
        'schedule': timedelta(seconds=5),
    },
}