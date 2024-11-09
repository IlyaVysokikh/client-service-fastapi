FROM python:3.13-slim-bullseye

WORKDIR /src

RUN apt update -y && \
    apt install -y python3-dev gcc musl-dev

COPY requirements.txt /src/
RUN pip install -r requirements.txt

COPY . /src/