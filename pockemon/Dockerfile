FROM python:3.7

RUN pip install django
COPY ./pockemon /app/pockemon
COPY ./manage.py /app

WORKDIR /app

EXPOSE 8000

CMD python manage.py runserver 0:8000