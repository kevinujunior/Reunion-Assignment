FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update && \
    apt install -y \
    gcc \
    libpq-dev && \
    apt-get clean

ENV PATH "$PATH:$HOME/.local/bin"

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

RUN python3 manage.py collectstatic --noinput

CMD gunicorn reuinion.wsgi:application --bind 0.0.0.0:8000