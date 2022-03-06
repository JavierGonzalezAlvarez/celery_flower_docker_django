# django celery and rabbitmq
sudo setxkbmap -layout 'es,es' -model pc105

## Create V.E
virtualenv entorno_virtual -p python3

## Activate V.E
source entorno_virtual/bin/activate

## Desativate V.E
deactivate

## install requirements
pip install -r requirements.txt 
pip install -U django-celery-results

## create project
$ django-admin startproject app1
$ app1/django-admin startapp app

# create db
sudo -u postgres psql
CREATE DATABASE celery WITH OWNER test;
DROP DATABASE celery;

## create user
python manage.py createsuperuser
javier
89_Lp%wD

## run django
$ python3 manage.py runserver

## install rabbitmq
$ sudo apt-get install -y erlang
$ sudo apt-get install rabbitmq-server

## install celery
sudo apt install python-celery-common

## activar rabbitmq-server
ps aux | grep rabbit
sudo kill -9 number_process


sudo ufw allow 5672/tcp
-chequear si hostname es correcto
$ sudo hostname --file /etc/hostname

$ systemctl status rabbitmq-server.service
o
$ sudo systemctl enabled rabbitmq-server

-confirm is running
$ systemctl is-enabled rabbitmq-server.service 

-en caso de error:
$ sudo hostname --file /etc/hostname

$ systemctl status rabbitmq-server

## consola del administrador
$ apt-get install erlang
$ sudo rabbitmq-plugins enable rabbitmq_management
$ sudo ufw allow proto tcp from any to any port 5672,15672

sudo rabbitmq-plugins enable rabbitmq_management


# uninstall rabbitmq-server
sudo apt-get remove --auto-remove rabbitmq-server
sudo apt-get purge --auto-remove rabbitmq-server

## run task 
$ celery -A conf worker -l info

$ python3 manage.py shell
from app.tasks import add
add.delay(4,4)

## create network
$ docker network create platform-network

## delete all containers
docker rm $(docker ps -a -q) -f

## delete all images
docker image ls
docker rmi $(docker images -q)

$ docker exec -it d4c9487fade6 /bin/bash

http://localhost:8000/
http://localhost:15672/
guest
guest
http://localhost:5555/

# spanish key VM - linux
sudo apt-get install console-data
sudo setxkbmap -layout 'es,es' -model pc105
sudo snap install --classic code

# install docker
$ sudo curl -sSL https://get.docker.com/ | sh
$ docker --version
$ sudo usermod -a -G docker $USER

# install docker-compose
$ sudo apt install docker-compose

# comandos rabbitmq (ok) (inside ve)
--------------------------------------
$ sudo rabbitmqctl list_queues

------------------
# RUN CELERY BEAT (ok)
--------------------------
celery -A conf beat -l INFO 
-in this case we set CELERYBEAT_SCHEDULE in "settings.py"
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



..................
# RUN CELERY (OK)
..................
celery -A conf worker --loglevel=info
celery -A conf worker --loglevel=DEBUG

# RUN CELERY BEAT (ok) (inside ve) - MORE THAN 1 WORKER (-B)
-no in production
----------------------------------------------------------------------
(no) celery -A conf worker -B -l info
celery -A proj beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

# RUN FLOWER (ok) (inside ve)
-----------------------------------
celery -A conf flower --broker=amqp://guest:guest@localhost:5672// --port=5555 --address=0.0.0.0

http://localhost:5555

## CHECK TASK
celery inspect reserved
celery inspect scheduled
celery inspect registered
celery inspect active

# + info
sudo hostname --file /etc/hostname
worker => celery@ubuntu