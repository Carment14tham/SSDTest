FROM ubuntu:latest
LABEL authors="khai"

ENTRYPOINT ["top", "-b"]

FROM python:3.10

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]