FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update
#RUN apt-get install -y gettext vim && apt-get clean
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install pip==20.2.4

COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY ./docker/django/entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["bash", "/entrypoint.sh"]
