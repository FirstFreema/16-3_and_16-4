# Используем базовый образ Python 3.12
FROM python:3.12-slim

# Устанавливаем apt-utils и необходимые пакеты для psycopg2
RUN apt-get update && apt-get install -y apt-utils && \
    apt-get install -y libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Указываем команду запуска Django сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
