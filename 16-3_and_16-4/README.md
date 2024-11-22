# DjangoRomaProject

DjangoRomaProject — это веб-приложение на Django, использующее Docker для контейнеризации и PostgreSQL в качестве базы данных. Проект включает автоматизацию создания базы данных, выполнения миграций и запуска сервера.

## Требования

- Docker
- Docker Compose

## Структура проекта

- **Dockerfile** — конфигурация для сборки образа веб-приложения Django.
- **docker-compose.yml** — настройка для запуска контейнеров веб-приложения и базы данных PostgreSQL.
- **.env_sample** — пример файла с переменными окружения.
- **requirements.txt** — список зависимостей для Django и других Python-библиотек, необходимых для проекта.

## Переменные окружения

Проект использует файл `.env` для хранения конфиденциальных данных и переменных окружения. Переменные включают:

- **POSTGRES_DB** — имя базы данных PostgreSQL.
- **POSTGRES_USER** — имя пользователя базы данных PostgreSQL.
- **POSTGRES_PASSWORD** — пароль для базы данных PostgreSQL.
- **DB_NAME** — имя базы данных для Django.
- **DB_USER** — пользователь базы данных для Django.
- **DB_PASSWORD** — пароль базы данных для Django.
- **DB_HOST** — хост базы данных для Django.
- **DB_PORT** — порт базы данных для Django.

## Установка и запуск

### 1. Склонируйте репозиторий

git clone <URL вашего репозитория>
cd <имя папки с проектом>

### 2. Настройка переменных окружения

Переименуйте файл .env_sample в .env и убедитесь, что он содержит корректные значения переменных окружения:

POSTGRES_DB=new_django_db
POSTGRES_USER=new_django_user
POSTGRES_PASSWORD=new_django_pass

DB_NAME=new_django_db
DB_USER=new_django_user
DB_PASSWORD=new_django_pass
DB_HOST=db
DB_PORT=5432

### 3. Запуск контейнеров

Запустите Docker Compose, чтобы собрать и запустить контейнеры:

docker-compose --env-file .env up --build

### 4. Доступ к приложению

После успешного запуска откройте в браузере:

http://localhost:8000

Часто используемые команды

Если необходимо вручную применить миграции, используйте команду:
docker-compose exec web python manage.py migrate

После изменения конфигурации Docker или переменных окружения выполните повторную сборку контейнеров:
docker-compose --env-file .env up --build

Для удаления контейнеров, сети и томов данных используйте команду:
docker-compose down -v

Для остановки контейнеров выполните:
docker-compose down