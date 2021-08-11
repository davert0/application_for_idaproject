# Описание

Тестовое задание

## Установка

```sh
git clone https://github.com/davert0/application_for_idaproject.git
```

## Запуск с помощью Docker
```
docker-compose up
```
Тесты в Docker
```
docker-compose exec app pytest
```
## Запуск без Docker

### Настройка окружения Linux


```sh
python -m venv env

source env/bin/activate

pip install -r requirements.txt
```
### Настройка окружения Windows

```
python -m venv env

env\Scripts\activate.bat

pip install -r requirements.txt
```

Запуск проекта

```sh
cd application_for_idaproject

python manage.py makemigrations

python manage.py migrate --run-syncdb

python manage.py runserver 8000
```

## Тесты

Запуск всех тестов

```sh
pytest
```
