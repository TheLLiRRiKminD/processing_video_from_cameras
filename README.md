# Проект "Обработка видео с RTS камеры"

Данный проект представляет собой веб-приложение обработки видео с одной открытой RTS камеры.
Система обрабатывает кадры и сохраняет в базу данных.

## О проекте

Бэкенд обеспечивает API для работы с видео для послеующего анализа

## Возможности

- Регистрация и авторизация пользователей
- Создание, чтение, обновление и удаление видео
- Автоматическую обработку при создании объекта видео
- Фильтрацию и выборку данных по заданной дате

## Технологии

- Python
- Django (Django REST framework, Celery)
- PostgreSQL (для хранения данных)

## Запуск проекта

1. Установите зависимости:
    - pip install -r requirements.txt

2. Создайте файл `.env` в корневой директории и заполните необходимые переменные окружения:
    - DJANGO_SECRET_KEY=
    - POSTGRES_DB=
    - POSTGRES_USER= 
    - POSTGRES_PASSWORD= 
    - POSTGRES_HOST= 
    - POSTGRES_PORT= 
    - SU_PASSWORD= 
    - SU_EMAIL_ADDRESS=
    - CELERY_BROKER_URL= 
    - CELERY_RESULT_BACKEND=
    - DJANGO_DEBUG= 
    - DJANGO_ALLOWED_HOSTS= 
    - TZ=

3. Примените миграции:
    - python manage.py migrate

4. Запустите сервер:
    - python manage.py runserver

5. Запустите Celery для обработки отложенных задач:
    - celery -A config worker --pool=solo -l INFO
    - celery -A config beat -l info -S django


## Документация API

Документация API доступна после запуска сервера по адресу: http://localhost:8000/redoc/