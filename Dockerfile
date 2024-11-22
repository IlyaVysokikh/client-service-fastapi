# Используем официальный образ Python 3.12
FROM python:3.13-slim-bullseye as builder

# Копируем файл зависимостей (если они уже есть)
COPY requirements.txt requirements.txt ./

# Устанавливаем необходимые пакеты и обновляем pip
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Разделяем контейнер на dev и prod
FROM python:3.13-slim-bullseye as dev

WORKDIR /app

# Окружение для предотвращения записи .pyc файлов и вывода ошибок в stdout
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /src
# Копируем зависимости для dev среды
COPY --from=builder requirements.txt /src/

# Устанавливаем зависимости для разработки
RUN apt update -y && \
    apt install -y python3-dev gcc musl-dev && \
    pip install --upgrade pip && pip install --no-cache-dir -r /src/requirements.txt

# Копируем весь проект в контейнер
COPY ./src /app/src

# Открываем порт 8000
EXPOSE 8000
