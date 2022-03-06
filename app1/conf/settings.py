"""
Django settings for app1 project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z-_anw06mnrmv1xp1hjn9%-d07u1t8a!!(+a@ir(5-&fc%az+)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.localhost', '127.0.0.1',
                 '127.0.0.1:8000', '[::1]', '0.0.0.0']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'django_celery_beat',
    'django_celery_results',    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

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

WSGI_APPLICATION = 'conf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'celery',
        'USER': 'test',
        'PASSWORD': '2525_ap',
        'HOST': 'localhost',
        # 'HOST': 'django-pg-celery',
        'PORT': '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# celery
# ---------------------------------------------------------------
broker_host = env('BROKER_HOST', default='rabbitmq')
# broker_host = env('BROKER_HOST', default='localhost')
broker_user = env('BROKER_USER', default='guest')
broker_password = env('BROKER_PASSWORD', default='guest')
broker_vhost = env('BROKER_VHOST', default='guest')


CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672/'

# CELERY_BROKER
#--------------------------
'''
CELERY_BROKER_URL = 'amqp://{0}:{1}@{2}:5672/{3}'.format(
    broker_user,
    broker_password,
    broker_host,
    broker_vhost
)
'''

# CELERY RESULT
# --------------------------
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'

#CELERY_DEFAULT_QUEUE = 'celery'
#CELERY_DEFAULT_QUEUE = 'guest'
#CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
#task_default_queue = 'guest'
#task_always_eager = True
#CELERY_ALWAYS_EAGER = env.bool('CELERY_ALWAYS_EAGER', False)

CELERY_TIMEZONE = "Europe/Madrid"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

# FLOWER
# ---------------------------------------------------------------
FLOWER_PORT = 5555
FLOWER_MAX_TASKS = 3600
# FLOWER_BASIC_AUTH = 'guest:guest'

FLOWER_BROKER_API = 'amqp://guest:guest@localhost:5672/'

'''
FLOWER_BROKER_API = "amqp://{0}:{1}@{2}:5672/{3}".format(
    broker_user,
    broker_password,
    broker_host,
    broker_vhost
)
'''

#from celery.schedules import crontab
#from datetime import timedelta

# MANUAL SCHEDULE
'''
CELERYBEAT_SCHEDULE = {
    'scheduled_task': {
        'task': 'run_task_add', # the same name that we have in the task.py
        #'schedule': crontab(hour=8, minute=31),
        'schedule': crontab(minute='*/15'), #Execute every 15 minutes        
        'args': (2,2)
        #'schedule': timedelta(seconds=3),
    },
    'scheduled_task': {
        'task': 'run_task_hi', # the same name that we have in the task.py
        'schedule': crontab(minute='*/1'),                
    },
}

CELERYBEAT_SCHEDULE = {
    'scheduled_task': {
        #'task': 'app.tasks.add',
        'task': 'run_task_add',
        'schedule': 6.0, #5 seconds
        'args': (10, 10),  # parameters for add()
    },
    'scheduled_task': {
        #'task': 'app.tasks.hi',
        'task': 'run_task_hi',
        'schedule': 5.0,
     },
}
'''