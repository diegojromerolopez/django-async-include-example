# syntax=docker/dockerfile:1
FROM python:3
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt install -y libpq-dev
RUN pip install -r requirements.txt
RUN mkdir -p /app/static
COPY . .
