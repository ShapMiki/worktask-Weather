FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/WeatherApp

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80
