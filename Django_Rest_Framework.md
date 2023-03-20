# Support service application

## Adjust the application

### Install deps

```bash
# Install pipenv
# https://pipenv.pypa.io/en/latest/
pip install pipenv
```

### Activate the environment

```bash
# Activate virtual env
pipenv shell
```

```bash
# Regenerate Pipfile.lock file
pipenv lock
```

```bash
# pipenv lock & pipenv sync
pipenv update
```

```bash
# pipenv sync
pipenv sync --dev
```

### Code quality tools

```bash
# https://pypi.org/project/flake8/
flake8

# https://pypi.org/project/black/
black

# https://pypi.org/project/isort/
isort
```

### Install framework

```bash
# https://pypi.org/project/Django/
Django
```

### Install additional packages

```bash
# https://pypi.org/project/psycopg-binary/
psycopg2-binary

# https://pypi.org/project/Pillow/
Pillow

# https://pypi.org/project/django-debug-toolbar/
django-debug-toolbar

# https://pypi.org/project/django-ckeditor/
django-ckeditor

# https://pypi.org/project/python-dotenv/
python-dotenv
```

## Creates a Django project

Create a folder src.
Creates a Django project directory structure for the given project name in the current directory or the given destination.

```bash
# https://docs.djangoproject.com/en/4.1/ref/django-admin/
django-admin startproject config src/
```

```bash
scr/
    config/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py
```

### The development server

Run the following commands:

```bash
python src/manage.py runserver
```

## Creates a Django apps

Creates a Django apps

```bash
django-admin startapp exchange_rates
```

Open up config/settings.py

```bash
INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
# Local
"exchange_rates.apps.ExchangeRatesConfig", # new
]
```

## Workflow

Django can create migrations for you. Make changes to your models - say, add a field and remove a model - and then run makemigrations:

``` python
python manage.py makemigrations
```

Once you have your new migration files, you should apply them to your database to make sure they work as expected:

``` python
python manage.py migrate
```

Set the STATIC_ROOT setting to the directory from which you’d like to serve these files, for example:

``` python
STATIC_ROOT = ROOT_DIR / "support_an/staticfiles"
```

Run the collectstatic management command:

```python
python src/manage.py collectstatic
```

## Как обрабатывается запрос от клиента в DRF

DRF (Django Rest Framework) - это фреймворк для создания веб-приложений RESTful API с помощью Django.

Когда клиент отправляет запрос к API, DRF использует классы Request и Response для обработки запросов и ответов соответственно.

Когда DRF получает запрос, он использует класс Request для создания экземпляра запроса и выполнения следующих действий:

1. Проверка типа запроса (GET, POST, PUT, DELETE и т.д.) и его параметров (query параметры, заголовки и т.д.).

2. Проверка соответствия URL запроса маршруту API и соответствия HTTP метода и метода API.

3. Проверка прав доступа к запрашиваемому ресурсу.

4. Проверка корректности запроса и его параметров.

5. Обработка запроса и извлечение данных из базы данных.

6. Обработка ошибок и возврат соответствующего HTTP-кода ответа.

Когда DRF обрабатывает запрос, он создает экземпляр класса Response для создания ответа. Класс Response используется для формирования HTTP-ответа и его параметров, таких как статусный код, заголовки и тело ответа.

Класс Response в DRF позволяет легко форматировать и возвращать данные в различных форматах, таких как JSON, XML и другие.

Кроме того, DRF предоставляет множество инструментов для сериализации, валидации и документирования данных, что упрощает работу с данными в API.

## Порядок прохождения запроса от клиента к url и далее, после чего ответ клиенту

Порядок прохождения запроса в Django Rest Framework обычно выглядит следующим образом:

1. Клиент отправляет HTTP-запрос, указывая URL-адрес, метод запроса, заголовки и тело запроса.

2. Django Rest Framework (DRF) получает запрос и сопоставляет URL-адрес запроса с зарегистрированными маршрутами в urls.py файле приложения Django.

3. Если URL-адрес соответствует одному из маршрутов, DRF передает запрос соответствующему представлению (view).

4. Представление получает запрос и выполняет нужные операции, например, чтение или запись данных в базу данных.

5. Представление создает и возвращает объект Response, содержащий данные для ответа на запрос, а также код состояния HTTP, заголовки и другие метаданные.

6. DRF обрабатывает объект Response и формирует соответствующий HTTP-ответ, отправляя его обратно клиенту.

7. Клиент получает ответ, обрабатывает его и выполняет нужные действия, например, выводит данные на экран или обрабатывает их дальше в своем приложении.

В общем случае, процесс обработки запроса в DRF заключается в обработке запроса, выполнении нужных действий на стороне сервера и формировании и отправке ответа обратно клиенту. При этом, Django Rest Framework обеспечивает широкий набор инструментов для работы с данными и упрощает создание RESTful API на базе Django.

## А как в процессе участвует serialization

В Django Rest Framework (DRF) serialization - это процесс преобразования сложных типов данных, таких как модели Django, в стандартные форматы данных, такие как JSON, XML и другие. Объекты сериализации в DRF являются основным механизмом для взаимодействия с данными в API.

Serialization в Django Rest Framework происходит следующим образом:

1. Когда DRF получает запрос, он передает его соответствующему представлению (view).

2. Представление выполняет нужные операции, например, чтение или запись данных в базу данных.

3. Представление создает объект сериализации, который описывает, как нужно преобразовать полученные данные в стандартный формат (например, JSON).

4. Объект сериализации применяется к данным, и данные преобразуются в соответствующий формат.

5. DRF создает и возвращает объект Response, содержащий преобразованные данные, а также код состояния HTTP, заголовки и другие метаданные.

Сериализация позволяет передавать данные между клиентом и сервером, а также сохранять их в базе данных в удобном формате. В DRF есть множество встроенных классов сериализации, которые обеспечивают преобразование данных в различные форматы. Кроме того, в DRF можно создавать пользовательские классы сериализации, которые позволяют настраивать преобразование данных по своему усмотрению.
