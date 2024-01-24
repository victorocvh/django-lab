FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt 

WORKDIR /app/django_web 

# Instalando Dockerize.
RUN apt-get update && apt-get install -y wget
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.6.1.tar.gz
RUN rm dockerize-linux-amd64-v0.6.1.tar.gz


CMD ["dockerize","-wait","tcp://djangodb:5432","python","manage.py","runserver","0.0.0.0:8000"]
