## Задача:

Нужно сделать HTTP сервис для сокращения URL наподобие [Bitly](https://bitly.com/) и других сервисов.

UI не нужен, достаточно сделать JSON API сервис.  
Должна быть возможность:

- сохранить короткое представление заданного URL
- перейти по сохраненному ранее короткому представлению и получить redirect на соответствующий исходный URL

### Выполнение:

Сделан JSON API сервис.

- Все написано на Python, с использованием фреймворка Django.
- В качестве БД выбрана PostgreSQL.
- Добавлена возможность запуска проекта через docker-compose (см. ниже).
- ~~Добавлены тесты (см. ниже) покрытие по report составляет примерно 89%.~~ Будут добавлены новые
- Добавлена валидация URL посредством инструментария Django.
- Существует возможность создания кастомной человекочитаемой ссылки

- Деплой с UI возможны в будущих итерациях проекта. UI будет построен на базе React.

### Запуск:

#### Собираем:

- \$docker-compose build

#### Делаем миграцию:

- \$docker-compose run web ./manage.py migrate

#### Запускаем:

- \$docker-compose up

### Определить степень покрытия приложения тестами

- \$docker-compose run web coverage run --branch --source=short_url ./manage.py test

- \$docker-compose run web coverage report

### Пример взаимодействия с API с помощью curl:

#### Получить сокращенный URL:

- \$curl -X POST -d base_url="https://github.com/avito-tech/auto-backend-trainee-assignment" localhost:8000/

##### Результат:

- http://0.0.0.0:8000/3743ad5ae2

#### Получить кастомную ссылку:

curl -X POST -d base_url="https://github.com/avito-tech/auto-backend-trainee-assignment" -d hash_url="avito-auto-be" http://0.0.0.0:8000

##### Результат:

- http://0.0.0.0:8000/avito-auto-be

#### Получить JSON всех добавленных URL:

- \$curl -X GET localhost:8000/

#### Удалить сокращённый URL из бд:

- \$curl -X DELETE http://0.0.0.0:8000/avito-auto-be

#### Изменить сокращенный URL на кастомный или :

1. - \$curl -X PUT -d hash_url="avito-auto" http://0.0.0.0:8000/avito-auto-be
2. - \$curl -X PUT -d hash_url="" http://0.0.0.0:8000/avito

##### Pезультат:

1. - http://0.0.0.0:8000/avito-auto
2. - http://0.0.0.0:8000/3743ad5ae2
