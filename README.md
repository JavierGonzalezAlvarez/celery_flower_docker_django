# django celery and rabbitmq

## Create V.E
virtualenv entorno_virtual -p python3

## Activate V.E
source entorno_virtual/bin/activate

## Desativate V.E
deactivate

## install requirements
pip install -r requirements.txt 
pip install celery

## create project
$ django-admin startproject app1
$ app1/django-admin startapp app

## run django
$ python3 manage.py runserver

## install rabbitmq
$ sudo apt-get install -y erlang
$ sudo apt-get install rabbitmq-server

## install celery
sudo apt install python-celery-common

## activar rabbitmq-server
$ sudo systemctl enabled rabbitmq-server
$ systemctl status rabbitmq-server

## consola del administrador
$ apt-get install erlang
$ rabbitmq-plugins enable rabbitmq_management
$ sudo ufw allow proto tcp from any to any port 5672,15672

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

$ docker exec -it f659e0ebfebd /bin/bash


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
