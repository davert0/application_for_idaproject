# Описание

Тестовое задание

## Установка

```sh
https://github.com/davert0/application_for_idaproject.git
```

## Запуск с помощью Docker
'''
docker-compose up
'''

Настройка окружения Linux

> python --version # Python 3.9.0

```sh
python -m venv env

source env/scripts/activate

pip install -r requirements.txt
```

Запуск проекта

```sh
cd imageapp

touch imageapp/.env

python manage.py makemigrations

python manage.py migrate --run-syncdb

python manage.py runserver 7000
```

## Тесты

Запуск всех тестов

```sh
py.test
```
