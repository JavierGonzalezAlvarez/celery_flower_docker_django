from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

#@shared_task
@shared_task(name='run_task_add')
def add(x, y):
    logger.info("task executed")
    print(x+y)
    return x+y

#@shared_task
@shared_task(name='run_task_hi')
def hi():
    print("hi")    
    return "hi"
