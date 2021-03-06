![](https://img.shields.io/badge/Python-3.8-blue) 
![](https://img.shields.io/badge/Django-2.2.16-green)
![](https://img.shields.io/badge/DjangoRestFramework-3.12.4-red)
![](https://img.shields.io/badge/Docker-3.8-yellow)
![](https://img.shields.io/badge/DockerCompose-2.5.0-yellow)

# api_yamdb
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.


# Инструкции по запуску
Для того чтобы развернуть образ на локальной машине, выполнитеследующиедействия.
1. Авторизоваться:
```sh
docker login
```
2. Загрузка образа с DockerHub
```sh
docker pull stasrls/infra:v1.01
```
3. Запустите Докер-контейнер:
```sh
docker-compose up -d
```
4. Выполинте последовательно миграции и создание суперпользователя:
```sh
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
5. Наполнить БД тестовыми данными выполнив команду:
```sh
python manage.py dbfill
```
6. Запустить проект:
```sh
python manage.py runserver
```
7. Проверьте доступность сервиса
```sh
http://localhost/admin
```

# Переменные среды
Этот образ использует переменные среды для настройки. Добавьте файл .env в папку infra и заполните переменные необходимыми значениями.

|Переменные              |Значение Default               |Описание                                            |
|------------------------|-------------------------------|----------------------------------------------------|
|`DB_ENGINE`             |`django.db.backends.postgresql`|Указываем БД                                 |
|`DB_NAME`               |`postgres`                     |Имя БД                                     |
|`POSTGRES_USER`         |no default                     |Логин                           |
|`POSTGRES_PASSWORD`     |no default                     |Пароль                          |
|`DB_HOST`               |`db`                           |Название хоста                       |
|`DB_PORT`               |5432                           |Порт для подключения к БД                           |

### Автор
[Шалгынов Станислав](https://github.com/stasrls)

### Лицензия
The Unlicense
