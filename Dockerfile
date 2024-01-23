FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt 

WORKDIR /app/django_web 

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
