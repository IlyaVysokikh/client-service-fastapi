# Используем официальный образ Python 3.12
FROM python:3.13-slim-bullseye as builder

COPY requirements.dev.txt requirements.dev.txt ./

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.dev.txt

FROM python:3.13-slim-bullseye as dev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /src

COPY --from=builder requirements.dev.txt /src/

RUN apt update -y && \
    apt install -y python3-dev gcc musl-dev && \
    pip install --upgrade pip && pip install --no-cache-dir -r /src/requirements.dev.txt

COPY ./src /app/src

EXPOSE 8000
