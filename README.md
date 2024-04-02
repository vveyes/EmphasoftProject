# Emphasoft

### Технологии:
+ Python
+ Django
+ DRF
+ PostgreSQL
___
### Инструкция по запуску приложения:

+ Клонируем репозиторий. (Проект сделан одним коммитом, так как проект небольшой).
+ Переходим в директорию проекта.
+ Создаем, затем активируем виртуальное окружение в терминале.

```
venv\Scripts\Activate
```
+ Установка зависимостей.
```pip install -r requirements.txt```
Database и Secret_key скрыты в .env файле. Пример, как он выглядит:
```angular2html

SECRET_KEY=django-insecure-c@_@kw^...


DB_NAME=blank
DB_USER=blank
DB_PASSWORD=blank
DB_HOST=localhost
DB_PORT=5432
```

+ Замените secret_key без кавычек, а также настройки database **Engine**, **Name**, **User**, **Password** на свои реальные.
+ Выполните миграции в терминале:
```angular2html
python manage.py makemigrations
python manage.py migrate
```
+ Запуск проекта:
```
python manage.py runserver
```
___

## Пользовательская документация

### Введение:

Проект представляет обеспечение, разработанное под функционал отеля, позволяющего:
+ Регистрироваться и авторизовываться
+ Просматривать комнаты в отеле.
+ Искать комнату по количеству мест и цене.
+ Бронировать комнату на определенный срок, если пользователь авторизован.
  + **Также в admin панеле Superuser может добавлять/удалять/редактировать комнаты и создавать бронь.**
+ Отменять бронирование - это может делать как пользователь, так и superuser.
  + **Superuser видит бронирование всех пользователей на данную комнату.**
___
### Маршруты:

+ Домашняя страница с redirect на список комнат:
```angular2html
http://localhost:8000/
```
+ Регистрация:
```angular2html
http://localhost:8000/registration/
```
+ Авторизация:
```angular2html
http://localhost:8000/login/
```
+ Профиль пользователя:
```angular2html
http://localhost:8000/profile/
```
+ Список комнат:
```angular2html
http://localhost:8000/rooms
```
+ Описание комнаты:
```angular2html
Детали комнаты: http://localhost:8000/room/[room_id]
```
