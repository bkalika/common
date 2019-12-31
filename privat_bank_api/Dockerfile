FROM python:3.7
EXPOSE 8000
COPY . /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
RUN ls -la
CMD python manage.py runserver 0:8000
