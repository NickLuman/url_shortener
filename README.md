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
- Добавлены тесты (см. ниже) покрытие по report составляет примерно 89%.
- Добавлена валидация URL посредством инструментария Django.

- Деплой с UI, а также человекочитаемые ссылки возможны в будущих обновлениях. UI будет построен на базе React.


### Запуск:

#### Собираем: 

- $docker-compose build

#### Делаем миграцию:

- $docker-compose run web ./manage.py migrate

#### Запускаем:

- $docker-compose up


### Определить степень покрытия приложения тестами
- $docker-compose run web coverage run --branch --source=short_url ./manage.py test

- $docker-compose run web coverage report


### Пример взаимодействия с API с помощью curl:

#### Получить сокращенный URL:
- $curl -X POST -d base_url=URL localhost:8000/

#### Получить JSON всех добавленных URL:
- $curl -X GET localhost:8000/

#### Получить исходный URL по сокращенному:
- $curl -X GET -d hash_url=SHORTENED_URL localhost:8000/