# Django Rest Framework

## Последлвательность обработки запроса клиента через DRF

Django Rest Framework (DRF) - это фреймворк для создания веб-сервисов на основе Django, который позволяет создавать API для взаимодействия с клиентами.

Обработка запроса клиента через DRF включает несколько шагов:

1. Нахождение соответствующего URL-шаблона: DRF находит соответствующий URL-шаблон в конфигурации URL-адресов Django, который будет использоваться для обработки запроса.

2. Создание объекта представления (view): после того, как был найден соответствующий URL-шаблон, DRF создает объект представления, который будет обрабатывать запрос.

3. Проверка разрешений (permissions): DRF проверяет разрешения, чтобы определить, может ли клиент выполнять запрашиваемую операцию. Если клиент не имеет прав на выполнение операции, DRF вернет ошибку авторизации.

4. Парсинг запроса(parser classes): DRF парсит данные запроса в формат, понятный для фреймворка. Например, если запрос содержит данные в формате JSON, DRF преобразует их в объект Python.

5. Валидация данных: DRF проверяет данные запроса на соответствие ожидаемым параметрам и типам данных. Если данные не соответствуют требованиям, DRF вернет ошибку валидации.

6. Обработка запроса: после успешной валидации, DRF передает данные представлению, которое выполняет требуемую операцию (создание, чтение, обновление или удаление данных), работа с базами данных.

7. Сериализация ответа (serializer classes): после выполнения операции, DRF преобразует данные ответа в формат, понятный для клиента. Например, если клиент ожидает ответ в формате JSON, DRF преобразует объект Python в JSON.

8. Возврат ответа: DRF возвращает ответ клиенту, который содержит результат выполненной операции.

В каждом из этих шагов можно настроить и изменить поведение DRF в соответствии с требованиями проекта.

## Парсинг запроса в Django Rest Framework (DRF)

Парсинг запроса в Django Rest Framework (DRF) происходит автоматически и зависит от типа данных, которые клиент отправляет на сервер. DRF может парсить данные в форматах JSON, HTML формах, XML, YAML и других.

DRF использует классы-парсеры (parser classes), чтобы автоматически определять тип данных, которые клиент отправляет на сервер, и преобразовывать их в формат, понятный для фреймворка. Классы-парсеры определяются в конфигурации DRF и могут быть настроены для поддержки специфических форматов данных.

По умолчанию DRF включает несколько классов-парсеров, таких как JSONParser, FormParser, MultiPartParser, которые позволяют автоматически парсить данные в формате JSON, HTML формах и многие другие. Когда клиент отправляет запрос, DRF автоматически выбирает соответствующий класс-парсер на основе заголовков запроса.

Например, если клиент отправляет запрос с заголовком "Content-Type: application/json", DRF будет использовать класс JSONParser для парсинга данных в формате JSON. Если заголовок "Content-Type" отсутствует или не указан, DRF выбирает класс-парсер, который имеет наивысший приоритет по умолчанию.

После парсинга данных, DRF создает объект Request, который содержит данные запроса и передает его в представление (view) для дальнейшей обработки. Если данные запроса не могут быть распарсены, DRF вернет ошибку парсинга.

## Валидация данных DRF

Django Rest Framework (DRF) предоставляет встроенный механизм валидации данных, который позволяет проверить, соответствуют ли данные запроса требуемым условиям и формату, определенному в представлении (view).

DRF использует классы-валидаторы (validator classes) для проверки данных запроса. Классы-валидаторы определяются в конфигурации DRF и могут быть настроены для поддержки специфических требований проекта.

При обработке запроса, DRF автоматически запускает механизм валидации, который включает несколько этапов:

1. Сериализация данных: DRF использует классы-сериализаторы (serializer classes) для преобразования данных запроса в формат, понятный для фреймворка.

2. Валидация данных: после сериализации данных, DRF автоматически применяет классы-валидаторы к полученным данным. Валидаторы могут проверять такие параметры, как наличие обязательных полей, правильность формата данных, ограничения по размеру и др.

3. Обработка ошибок валидации: если валидация не проходит, DRF возвращает ошибку валидации вместе с соответствующим сообщением об ошибке.

Например, представление, которое обрабатывает запрос на создание нового объекта, может содержать класс-сериализатор и класс-валидатор для проверки правильности ввода данных. Если клиент отправляет запрос с некорректными данными, DRF вернет сообщение об ошибке валидации, указывая на конкретные проблемы.

Кроме встроенных классов-валидаторов, DRF также позволяет создавать собственные классы-валидаторы для обработки специфических требований проекта.