from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('conf')
#app = Celery('test_celery',broker='amqp://admin:mypass@10.211.55.12:5672',backend='rpc://',include=['test_celery.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

# creamos una instancia
app.autodiscover_tasks()
