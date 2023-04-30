### book

## Стэк
```
Python 3.9, Django 3.2, Django REST Framework 3.12.0, PostgresQL 15.0, Djoser.
```
## Развертывание проекта
```
1. git clone git@github.com:Sapik-pyt/book.git
```
```
2.python -m pip install --upgrade pip
```
```
3.pip install -r requirements.txt
```
```
4.python manage.py createsuperuser
```
```
5.Заменить файл env.example на .env и заполнить поля
```
# settings.py
SECRET_KEY='<secret_key>'      # стандартный ключ, который создается при старте проекта
ENGINE=django.db.backends.postgresql
DB_NAME                        # имя БД - postgres (по умолчанию)
POSTGRES_USER                  # логин для подключения к БД - postgres (по умолчанию)
POSTGRES_PASSWORD              # пароль для подключения к БД (установите свой)
DB_HOST=db                     # название сервиса (контейнера)
DB_PORT=5432                   # порт для подключения к БД
```
```
6.python manage.py runserver
```
