# FastAPI

## Что такое FastAPI?

**`FastAPI`** - это быстрый (fast) и простой в использовании фреймворк для создания веб-приложений на языке Python. Он основывается на стандарте Python для типизации данных (Python Type Hints) и поддерживает асинхронное программирование.

FastAPI имеет множество функций, которые делают его удобным для разработки веб-приложений, включая автоматически сгенерированные документы OpenAPI и Swagger UI, валидацию данных на основе схем JSON, встроенную поддержку CORS, автоматический парсинг запросов и многое другое.

FastAPI также предоставляет поддержку многопоточности и позволяет создавать высокопроизводительные веб-приложения, которые могут обслуживать большое количество запросов за короткий промежуток времени.

## Какой язык программирования использует FastAPI?

**`FastAPI`** — это веб-фреймворк для создания API с Python 3.7+ на основе стандартных аннотаций типов Python.

**`API`** - это сокращение от "Application Programming Interface", что означает  **`интерфейс программирования приложений`**. Это набор инструментов, протоколов и стандартов, которые позволяют программистам создавать программное обеспечение, которое взаимодействует с другими программами, приложениями и сервисами.

API определяет, как различные компоненты программного обеспечения могут взаимодействовать друг с другом, определяет форматы данных, которые могут быть переданы, и какие операции могут быть выполнены с этими данными.

## Каковы особенности FastAPI?

- Быстро и эффективно

- Легко использовать

- Интуитивно понятные API с использованием подсказок типа Python

- Автоматическая проверка данных, сериализация и документирование

- Поддержка GraphQL включена по умолчанию.

- Встроенная поддержка синтаксиса async/await.

## Каковы преимущества использования FastAPI?

FastAPI - это фреймворк для создания веб-приложений на языке Python, который обеспечивает высокую производительность и быстрое развертывание.

Он предоставляет множество преимуществ, включая:

- Быстрое развертывание: FastAPI предоставляет простой и интуитивно понятный API, который позволяет быстро развернуть приложение.

- Высокая производительность: благодаря использованию асинхронной обработки запросов и использованию статической типизации, FastAPI обеспечивает высокую производительность и быструю обработку запросов.

- Автоматическая документация: FastAPI автоматически создает документацию для API на основе аннотаций типов данных и входных параметров, что упрощает их использование и понимание.

- Поддержка OpenAPI и JSON Schema: FastAPI поддерживает стандарты OpenAPI и JSON Schema, что обеспечивает совместимость с другими инструментами и библиотеками.

- Интеграция с базами данных: FastAPI имеет интеграцию с различными базами данных, такими как PostgreSQL, MySQL, SQLite и MongoDB, что позволяет быстро и легко подключать их к приложению.

- Поддержка WebSocket: FastAPI поддерживает протокол WebSocket, что позволяет создавать приложения с двусторонней связью между сервером и клиентом.

В целом, FastAPI является быстрым и эффективным инструментом для разработки веб-приложений на Python, который предоставляет широкие возможности для интеграции с другими инструментами и технологиями.

## Какие базы данных поддерживает FastAPI?

FastAPI поддерживает любой сервер базы данных, совместимый с SQLAlchemy ORM, такой как PostgreSQL, MySQL, SQLite и т. д.

## Чем FastAPI отличается от других веб-фреймворков, таких как Flask и Django?

**`FastAPI`** - это современный веб-фреймворк на языке Python, который был создан в качестве альтернативы Flask и Django. Он отличается от них следующими особенностями:

- Высокая скорость: FastAPI использует асинхронную обработку запросов и ответов, благодаря чему обрабатывает запросы значительно быстрее, чем Flask и Django.

- Типизация данных: FastAPI использует Python 3.7+ и встроенные аннотации типов, что позволяет создавать строго типизированные API и улучшает поддержку интегрированной разработки средствами разработки (IDE).

- Документация API: FastAPI автоматически генерирует документацию API, основываясь на аннотациях типов и некоторых других метаданных, что значительно упрощает разработку и тестирование.

- Встроенная поддержка WebSocket: FastAPI имеет встроенную поддержку WebSocket и позволяет легко создавать реальновременные приложения.

- Автоматическое валидирование данных: FastAPI автоматически проверяет данные, полученные от клиента, на соответствие аннотированным типам, что значительно упрощает обработку ошибок во время разработки и уменьшает количество ошибок в продакшене.

- Поддержка многопоточности: FastAPI позволяет запускать несколько рабочих процессов и многопоточно обрабатывать запросы, что увеличивает пропускную способность и скорость обработки.

- Использование стандартных инструментов: FastAPI использует стандартные инструменты Python, такие как Pydantic для сериализации и валидации данных, и Starlette для работы с асинхронными запросами и ответами.

В целом, FastAPI является современным и быстрым веб-фреймворком с множеством полезных функций и особенностей, которые делают его удобным и эффективным для разработки современных веб-приложений.

## Что такое асинхронное программирование и как с ним справляется FastAPI?

**`Асинхронное программирование`** - это подход к разработке программного обеспечения, в котором задачи могут выполняться параллельно и независимо друг от друга без необходимости ожидания завершения предыдущих задач. Это достигается с помощью использования асинхронных функций и асинхронных вызовов, которые позволяют программе работать более эффективно и быстро отвечать на запросы.

FastAPI также предлагает множество инструментов для управления асинхронными задачами, такими как завершение задач при помощи **`asyncio`**, использование **`background tasks`** для выполнения фоновых операций, а также возможность обработки запросов в реальном времени при помощи **`WebSocke`t**.

Благодаря использованию асинхронного программирования FastAPI позволяет создавать высокопроизводительные веб-приложения, которые могут обрабатывать большие объемы запросов одновременно.

## Что такое WebSocket и как он применяетьсся в FastAPI

**`WebSocket`** - это протокол двунаправленной связи между клиентом и сервером, который позволяет установить постоянное соединение между ними и обмениваться данными в режиме реального времени. Это позволяет создавать интерактивные веб-приложения, такие как чаты, онлайн-игры, мониторинг систем и т.д.

FastAPI полностью поддерживает работу с WebSocket и предоставляет удобные инструменты для создания веб-приложений на основе этой технологии. Для работы с WebSocket в FastAPI используется библиотека **`fastapi.websockets.`**

Для создания WebSocket-соединения в FastAPI необходимо создать функцию-обработчик, которая будет вызываться при установке соединения с клиентом. Для этого можно использовать декоратор **`@app.websocket()`**, где app - экземпляр FastAPI-приложения.

Пример:

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")
```

В данном примере мы создаем функцию-обработчик websocket_endpoint, которая принимает экземпляр WebSocket в качестве параметра. Внутри функции мы вызываем метод accept() для установки соединения с клиентом, а затем запускаем бесконечный цикл, в котором мы принимаем сообщения от клиента при помощи метода receive_text() и отправляем им ответ при помощи метода send_text().

Таким образом, FastAPI позволяет легко создавать веб-приложения, которые могут работать с WebSocket и обмениваться данными в режиме реального времени.

## Как установить FastAPI?

Вы можете установить FastAPI через pip | pienv:

```code
pip install fastapi

pipenv install fastapi
```

## Какова цель зависимости в FastAPI?

**`Зависимость`** — это функция, которая предоставляет определенный ресурс для маршрута.

## Как вы определяете маршрут в FastAPI?

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    ...
```

## Как получить доступ к параметрам запроса в FastAPI?

Вы можете использовать метод request_params из модуля fastapi:

```python
from fastapi import FastAPI, Request

@app.get('/')
async def get_query_params(request: Request):

    limit = request.query_params.get('limit')
    offset = request.query_params.get('offset')

    return {"limit": limit, "offset": offset}
```

## Как вы используете запросы HTTP Post в FastAPI?

Вы можете использовать запрос POST от FastAPI для отправки данных на сервер.

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```

## Как вы проверяете входящие данные в FastAPI?

FastAPI использует Pydantic, библиотеку проверки данных, для проверки входящих данных. Вы можете использовать декораторы, такие как `@constrains`.

```python
from pydantic import BaseModel, constrains

class Item(BaseModel):
    name: str
    price: float
    description: str = None

    @constrains('name')
    def validate_name(cls, value):
        assert len(value) > 1, 'Name must be at least 2 characters'
```

## Что такое Pydantic?

**`Pydantic`** библиотека проверки данных, которая поддерживает FastAPI.

## Как добавить промежуточное программное обеспечение в Fastapi?

Вы можете использовать метод `fastapi.add_middleware` для добавления промежуточного программного обеспечения в Fastapi.

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Какова цель фоновой задачи в Fastapi и как вы его используете?

**`Фоновая задача`** - это функция, которая асинхронно работает с основным приложением.Вы можете использовать метод `founaltasks.add_task`, чтобы добавить фоновую задачу в Fastapi.

```python
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.post("/send-email")
async def send_email(background_tasks: BackgroundTasks, email: str, message: str):
    background_tasks.add_task(write_notification, email, message)
    return {"message": "Email sent in the background"}
```

## Какова цель параметра пути в Fastapi и как вы его используете?

Параметр пути является частью пути URL, который используется для идентификации ресурса. Вы можете определить параметры пути, заключив их в кудрявые скобки {}.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user": user_id}
```

## Как получить доступ к объекту запроса в FASTAPI?

Вы можете использовать класс запросов из модуля FASTAPI для доступа к объекту запроса.

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def read_root(request: Request):
    client_host = request.client.host
    return {"client_host": client_host}
```

## Какие типы ответов поддерживают FastAPI?

FastAPI поддерживает большинство типов ответов: строка, список, словарь, Pydantic модели, байты или даже файлы.

## How do you define response models in FastAPI?

Вы можете определить модели откликов, создав класс Pydantic Model и указав его как возвращаемый тип конечной точки API.

```python
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    tax: float = None

app = FastAPI()

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    ...
```

## Что такое асинхронная структура?

Асинхронная структура-это программная структура, которая одновременно управляет группой задач ввода/вывода для оптимизации использования ресурсов и масштабируемости.

## Как вернуть исключение в Fastapi?

Вы можете поднять Httpexception, чтобы вернуть исключение.

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
```

## Как получить доступ к параметрам заголовка в Fastapi?

Вы можете использовать словарь request.Headers для доступа к параметрам заголовка.

```python
from fastapi import Header, FastAPI

app = FastAPI()

@app.get("/")
async def read_root(user_agent: str = Header(None)):
    return {"User-Agent": user_agent}
```

## Как вы используете аутентификацию OAuth2 в FASTAPI?

Вы можете использовать аутентификацию OAuth2 в FASTAPI, установив расширение `oauth2`.

```code
pipenv install python-jose[cryptography]

pipenv install oauthlib

pipenv install fastapi_oauth2
```

```python
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
```

## Как вы реализуете WebSocket в Fastapi?

Вы можете внедрить WebSocket в FastAPI, внедрив конечную точку WebSocket.

```python
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
```

## Как вернуть файл в Fastapi?

Вы можете использовать метод `FileResponse 'из модуля FASTAPI.Responses, чтобы вернуть файл.

```python
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/download")
async def download_pdf():
    filename = "example.pdf"
    return FileResponse(filename)
```

## Как вы справляетесь с CORS в Fastapi?

Вы можете использовать промежуточное программное обеспечение `fastapi.middleware.cors.corsmiddleware` для обработки CORS в FastAPI.

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Как писать тесты для Fastapi?

Вы можете использовать `pytest` структура тестирования и `pytest-asyncio` плагин для записи тестов для FastAPI.

Пример:

```python
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
```

## Как вы генерируете документацию OpenAPI в FASTAPI?

Fastapi генерирует документацию OpenAPI автоматически.Вы можете просмотреть документацию, просматривая `http://localhost:8000/docs`.

## Как настраивать документацию OpenAPI в FastAPI?

Вы можете настроить документацию OpenAPI в FASTAPI, используя `Swagger UI` интерфейс.

Пример:

```python
app = FastAPI(
    title="My Awesome Application",
    description="This is a very awesome application",
    version="0.1.0"
)

app.openapi_tags = [
    {"name": "users", "description": "Users operations"},
    {"name": "items", "description": "Items operations"},
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: Item):
    return item
```

Что такое FastAPI's Route39?

**`Route39`** это новая функция, добавленная в Fastapi v0.65.0, которая позволяет вам определять маршруты, используя имя функции вместо аннотации.

## Как вы реализуете аутентификацию пользователя в FastAPI?

Вы можете реализовать аутентификацию пользователя в FASTAPI, добавив зависимость для проверки учетных данных пользователя.

Пример:

```python
async def get_user(email: str):
    user = await User.get_or_none(email=email)
    return user

async def authenticate_user(email: str, password: str):
    user = await get_user(email)
    return user

async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=400, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = await get_user(email=email)
    if user is None:
        raise HTTPException(status_code=400, detail="Invalid token")
    return user

@app.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    access_token = await create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
```

## Как вы используете фоновые задачи в Fastapi?

Вы можете использовать фоновые задачи в FASTAPI, определив функцию и зарегистрировав ее с помощью метода `BackgroundTasks.add_task`.

Пример:

```python
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.post("/send-email")
async def send_email(background_tasks: BackgroundTasks, email: str, message: str):
    background_tasks.add_task(write_notification, email, message)
    return {"message": "Email sent in the background"}
```

## Как вы обрабатываете загрузку файлов в FastAPI?

Вы можете обрабатывать загрузки файлов в FastAPI, определив маршрут, который получает объект файла.

Пример:

```python
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
```

## How do you use FastAPI with SQLAlchemy?

Вы можете использовать FASTAPI с SQLAlchemy, определив соединение с базой данных SQL и используя инъекцию зависимостей для доступа к соединению.

Пример:

```python
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(email=user.email, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
```

## Как вы используете Pytest с FastAPI?

Вы можете использовать Pytest для тестирования приложений FASTAPI, указав приспособление `client`, который возвращает `TestClient '.

Пример:

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
```

## Как вы обрабатываете миграции базы данных в Fastapi?

Вы можете обрабатывать миграции базы данных в FASTAPI, используя Alembic для генерации и применения сценариев SQL.

Пример:

```code
pipenv install alembic

alembic init alembic

alembic revision -m "initial revision"

alembic upgrade head

alembic revision -m "add columns to user table"

alembic upgrade head
```

## Как добавить пользовательский обработчик исключений в Fastapi?

Вы можете добавить пользовательский обработчик исключений в Fastapi, определив функцию, которая принимает `HTTPException` параметр и возвращает `JSONResponse`.

Пример:

```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )
```

## Как добавить пользовательское промежуточное программное обеспечение в Fastapi?

Вы можете добавить пользовательское промежуточное программное обеспечение в Fastapi, определив класс, который наследует от `StarletteMiddleware`.

Пример:

```python
from fastapi import FastAPI, Request
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        response = await call_next(request)

        # Do something with the response

        return response

app = FastAPI()

app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(CustomMiddleware)
```

## Как вы используете JWT с FASTAPI?

Вы можете использовать JWT для обработки авторизации в Fastapi.Вы можете использовать `PyJWT` библиотека, чтобы кодировать и декодировать токены JWT.

Пример:

```code
pip install PyJWT
```

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import JWTAuthentication, JWTBearer
from passlib.hash import bcrypt
import jwt

app = FastAPI()

JWT_SECRET_KEY = "secret_key"
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

users_db = [
    {
        "username": "john_doe",
        "email": "johndoe@example.com",
        "hashed_password": bcrypt.hash("secret"),
    },
]

def authenticate_user(email: str, password: str):
    for user in users_db:
        if user["email"] == email and bcrypt.verify(password, user["hashed_password"]):
            return user
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

@app.post("/login")
def login(email: str, password: str):
    user = authenticate_user(email, password)
    access_token = jwt.encode(
        {
            "sub": user["email"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        }, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return {"access_token": access_token}

async def get_current_user(token: str = Depends(JWTBearer())):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    user = next((user for user in users_db if user["email"] == email), None)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user

@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user
```

## Как вы выполняете маршрутизацию в Fastapi?

Вы можете выполнять маршрутизацию в FastAPI, определив маршруты, используя `@app.route` decorator.

Пример:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

## В чем разница между параметром пути и параметром запроса в FastAPI?

В FastAPI параметр пути и параметр запроса используются для передачи данных в HTTP запросах, но они имеют различия в использовании и семантике.

**`Параметры пути (Path parameters)`** используются для передачи данных, которые являются неотъемлемой частью маршрута. Они указываются в пути URL и заключены в фигурные скобки. Например:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

В этом примере мы определяем маршрут **`/items/{item_id}`**, где **`item_id является параметром пути`**. В запросе GET **`/items/42`** значение параметра item_id будет равно 42.

Параметры запроса (Query parameters) используются для передачи дополнительных данных в запросе. Они указываются в URL после символа `?` и могут быть опциональными. Например:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

В этом примере мы определяем маршрут **`/items/`**, где **`skip и limit являются параметрами запроса`**. Параметры запроса могут иметь значения по умолчанию, как в примере, где skip=0 и limit=10. В запросе GET **`/items/?skip=20&limit=30`** значение skip будет равно 20, а значение limit будет равно 30.

Важно отметить, что FastAPI автоматически выполняет валидацию и преобразование типов данных для параметров пути и запроса, что упрощает обработку входных данных.

## Как вы можете обрабатывать ошибки и исключения в FastAPI?

FastAPI использует стандартный подход Python для обработки ошибок и исключений. Вы можете использовать конструкцию **`try-except`** для обработки исключений и использовать декораторы для обработки ошибок.

Например, чтобы обработать исключение в FastAPI, вы можете использовать следующий код:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    try:
        # some code that might raise an exception
    except Exception as e:
        # handle the exception
        return {"error": str(e)}
```

В этом примере мы обрабатываем все исключения, которые могут возникнуть в блоке try, используя конструкцию except. Мы также возвращаем сообщение об ошибке в формате JSON с помощью объекта {"error": str(e)}.

Кроме того, FastAPI также предоставляет декораторы, такие как **`HTTPException`**, который может использоваться для обработки ошибок, связанных с HTTP-запросами. Например:

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
```

В этом примере мы используем декоратор HTTPException для генерации исключения, если запрошенный item_id не найден в базе данных. Мы также указываем код состояния 404 и детали ошибки в формате JSON.

В целом, FastAPI предоставляет широкие возможности для обработки ошибок и исключений, что делает его очень гибким и мощным инструментом для разработки веб-приложений.

## Как вы можете защитить свое приложение FastAPI?

Существует множество методов защиты приложения FastAPI, вот некоторые из них:

1. Использование **`HTTPS`**: HTTPS шифрует передачу данных между клиентом и сервером, защищая их от прослушивания и изменения. Для обеспечения безопасности приложения FastAPI необходимо использовать HTTPS вместо HTTP. Для этого можно использовать SSL-сертификаты, которые можно получить у авторитетного центра сертификации.

2. Использование **`токенов`** авторизации: Токены авторизации - это уникальные строки, которые выдаются пользователю после успешной аутентификации. При каждом запросе к API пользователь должен отправлять этот токен, чтобы сервер мог проверить его подлинность. Это позволит предотвратить несанкционированный доступ к API.

3. Ограничение доступа по **`IP-адресу`**: Можно ограничить доступ к API только для определенных IP-адресов. Это поможет предотвратить несанкционированный доступ к API извне.

4. Использование **`корректных прав доступа`**: Если приложение FastAPI взаимодействует с базой данных, то необходимо убедиться, что у пользователя, под которым работает приложение, есть только необходимые права доступа к базе данных. Это поможет предотвратить несанкционированный доступ к базе данных.

5. Регулярное **`обновление приложения`**: Регулярное обновление приложения поможет предотвратить известные уязвимости в сторонних библиотеках и фреймворках, которые используются в приложении.

6. Проведение **`тестирования на проникновение`**: Тестирование на проникновение - это процесс поиска уязвимостей в приложении путем попыток несанкционированного доступа. Проведение тестирования на проникновение поможет выявить слабые места в приложении и принять меры для устранения уязвимостей.

## Можете ли вы объяснить концепцию промежуточного программного обеспечения в FastAPI?

**`Промежуточное программное обеспечение (Middleware)`** в FastAPI - это функция, которая может быть вызвана перед или после обработки запроса. Она имеет доступ к запросу и ответу, и может модифицировать их или выполнить какую-то логику на основе их содержимого.

В FastAPI, middleware может быть определен как функция, которая принимает два аргумента: запрос (Request) и функцию-обработчик (handler). Middleware может модифицировать запрос перед его обработкой в функции-обработчике и модифицировать ответ после ее выполнения.

Пример использования middleware в FastAPI:

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Custom-Header"] = "Hello World"
    return response
```

В этом примере, мы создаем `middleware` функцию `add_custom_header`, которая добавляет к заголовкам ответа кастомный заголовок с текстом "Hello World". Мы регистрируем эту функцию как middleware для обработки HTTP запросов через декоратор @app.middleware("http"). Функция call_next передает управление следующему middleware или функции-обработчику.

При использовании этого middleware в FastAPI, каждый HTTP ответ будет содержать новый заголовок Custom-Header, содержащий текст "Hello World".

Использование middleware в FastAPI позволяет добавлять различную логику обработки запросов, такую как аутентификацию, логирование, мониторинг и многое другое.

## Что такое внедрение зависимостей в FastAPI?

**`Внедрение зависимостей`** (Dependency Injection) в FastAPI - это подход, который позволяет объявлять зависимости вашего приложения вне области видимости ваших эндпоинтов и импортировать их туда только при необходимости.

С помощью внедрения зависимостей вы можете избежать необходимости создавать объекты и устанавливать связи между ними в каждом эндпоинте, где они необходимы. Вместо этого, вы можете определить эти объекты где-то в другом месте вашего приложения, а затем передать их в ваш эндпоинт в качестве зависимости.

В FastAPI вы можете определить зависимости как функции, которые возвращают объекты, необходимые для вашего приложения. Вы можете указать, какие зависимости необходимы для каждого эндпоинта, используя аннотации типов и декораторы.

FastAPI автоматически обрабатывает внедрение зависимостей и обеспечивает, чтобы объекты были созданы только один раз и использовались многократно во всем приложении. Это делает ваш код более модульным, легким для тестирования и легко поддерживаемым.

## Как добавить поддержку CORS в приложение FastAPI?

**`CORS`** (Cross-Origin Resource Sharing) - это механизм, который позволяет веб-странице получать ресурсы с другого источника, не совпадающего с источником страницы.

По умолчанию, из-за политики безопасности браузера, скрипты на странице не могут получать доступ к ресурсам, находящимся на других доменах или портах. Это ограничение существует для предотвращения возможных атак на пользовательские данные, которые могут быть получены через непроверенные источники.

CORS позволяет серверам указывать, какие конкретно источники (домены, порты, протоколы) могут получать доступ к определенным ресурсам на сервере. Это позволяет контролировать безопасность и предотвращать атаки.

Реализация CORS происходит путем добавления определенных заголовков к HTTP-ответу сервера. Когда браузер получает ответ с этими заголовками, он может разрешить доступ к ресурсам для скриптов, работающих на другом домене.

Для добавления поддержки CORS в приложение FastAPI вы можете использовать модуль "fastapi.middleware.cors".

Вот пример кода, который показывает, как использовать CORS-мидлвар в FastAPI:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Добавляем CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ваш код FastAPI здесь
```

В приведенном выше примере мы создали экземпляр FastAPI и добавили CORS-мидлвар в приложение с параметрами:

allow_origins=["*"]: разрешаем запросы из любого источника.
allow_credentials=True: разрешаем передачу куки и заголовков аутентификации с запросами CORS.
allow_methods=["*"]: разрешаем использование любого метода HTTP.
allow_headers=["*"]: разрешаем использование любых заголовков.
Можно настроить параметры мидлвара в зависимости от ваших потребностей. Важно знать, что разрешение доступа со звездочкой (*) может создать небезопасные условия и следует быть осторожным при использовании его в производственной среде.

## Как вы можете выполнить проверку ввода в FastAPI?

FastAPI предоставляет множество инструментов для проверки ввода, чтобы гарантировать, что данные, поступающие от клиентов, соответствуют ожиданиям вашего приложения.

Одним из наиболее распространенных способов проверки входных данных в FastAPI является использование модуля pydantic. `Pydantic` - это библиотека Python, которая предоставляет декларативный способ определения данных, которые вводятся и выводятся в вашем приложении. Она может использоваться как для проверки входных данных, так и для валидации данных, которые возвращаются из вашего API.

Чтобы использовать Pydantic для проверки входных данных в FastAPI, вы можете создать класс модели, который описывает ожидаемые данные, и добавить его как аргумент для функции маршрутизатора FastAPI. Например, чтобы создать маршрут, который ожидает JSON-объект, содержащий поля name и age, вы можете создать следующую модель:

```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
Затем вы можете использовать эту модель как аргумент для функции маршрутизатора FastAPI:

python
Copy code
from fastapi import FastAPI
from .models import Person

app = FastAPI()

@app.post("/people/")
async def create_person(person: Person):
    return {"name": person.name, "age": person.age}
```

В этом примере функция create_person ожидает объект Person в качестве аргумента и возвращает словарь с полями name и age. Если входные данные не соответствуют ожидаемой модели, FastAPI автоматически создаст исключение ValidationError, которое можно перехватить и обработать соответствующим образом.

Вы также можете использовать декораторы FastAPI, такие как @query_parameter, @path_parameter и @header, чтобы проверить значения параметров запроса, переданных в ваше приложение. Например:

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None, user_agent: str = Header(None)):
    return {"item_id": item_id, "q": q, "user_agent": user_agent}
```

В этом примере item_id - это обязательный путь, а q и user_agent - опциональные параметры запроса. FastAPI автоматически проверит, что item_id является целым числом, а user_agent - строкой. Если значения параметров не соответствуют ожидаемому типу, FastAPI создаст исключение ValueError.

## Как вы можете обрабатывать загрузку файлов в FastAPI?

FastAPI предоставляет удобные инструменты для обработки загрузки файлов веб-приложениями. Для этого можно использовать модуль **`fastapi.UploadFile`**.

Вот простой пример, который показывает, как загрузить файл с помощью FastAPI:

```python
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
```

В этом примере создается маршрут POST /uploadfile/, который принимает объект UploadFile в качестве параметра. При использовании функции File(...), мы сообщаем FastAPI, что параметр является файлом, который необходимо загрузить.

После загрузки файла, мы возвращаем объект JSON, содержащий имя файла (file.filename). Можно также использовать объект file для выполнения других операций, таких как чтение или запись содержимого файла.

Важно отметить, что при загрузке больших файлов может потребоваться дополнительная настройка FastAPI, чтобы избежать проблем с памятью и производительностью. Например, можно использовать параметр stream=True для обработки файлов крупнее размера памяти. Кроме того, необходимо учитывать ограничения на размер загружаемых файлов, чтобы не допустить переполнения памяти или сбоев в работе веб-сервера.

## Можете ли вы объяснить концепцию фоновых задач в FastAPI?

**`Фоновые задачи`** - это задачи, которые выполняются асинхронно, без блокировки основного потока выполнения приложения. Таким образом, они позволяют выполнять длительные задачи, такие как обработка больших объемов данных или отправка электронной почты, без задержки работы приложения и ожидания завершения задачи.

FastAPI предоставляет интеграцию с библиотекой `Celery` для запуска фоновых задач. `Celery` - это распределенная система управления задачами, которая позволяет запускать задачи асинхронно и масштабировать приложения.

Для создания фоновой задачи в FastAPI необходимо использовать декоратор @app.task() и определить функцию, которая будет выполняться асинхронно. Пример такой функции:

```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def process_data(background_tasks: BackgroundTasks, data: dict):
    # выполняем длительную задачу
    result = do_something_with_data(data)
    # отправляем результат по электронной почте
    background_tasks.add_task(send_email, result)
```

Затем можно вызвать эту функцию из обработчика API и передать данные в качестве параметра. Например:

```python
@app.post("/process-data")
async def process_data_route(data: dict, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_data, data)
    return {"message": "Задача добавлена в очередь"}
```

В этом примере мы передаем данные в функцию process_data через параметр data.

## Как реализовать пагинацию в FastAPI?

Для реализации пагинации в FastAPI можно использовать параметры запроса (query parameters) в сочетании с Pydantic моделями для валидации.

Ниже приведен пример кода для реализации пагинации в FastAPI с помощью параметров запроса:

```python
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class PaginationParams(BaseModel):
    page: Optional[int] = 1
    page_size: Optional[int] = 10

@app.get("/items/")
async def read_items(pagination: PaginationParams):
    # Вычисляем значения границ для пагинации
    limit = pagination.page_size
    offset = (pagination.page - 1) * pagination.page_size

    # Выполняем запрос к базе данных, используя limit и offset для пагинации
    items = await get_items_from_database(limit=limit, offset=offset)

    return {"items": items}
```

В этом примере мы определяем модель PaginationParams, которая содержит два параметра для пагинации: page и page_size. Мы устанавливаем значения по умолчанию, чтобы предотвратить ошибки, если они не будут указаны в запросе. Затем мы создаем маршрут /items/, который ожидает параметр pagination с типом PaginationParams.

## Какова роль Pydantic в FastAPI?

Pydantic является ключевой библиотекой, используемой в FastAPI для обеспечения синтаксического анализа и валидации данных входных параметров (request payloads) и выходных данных (response payloads).

FastAPI использует Pydantic модели для определения схемы данных (data schemas) для входных и выходных параметров API. Pydantic предоставляет ряд функций валидации данных, которые позволяют легко проверять, соответствует ли входной запрос определенной модели данных. Например, можно проверить, что запрос содержит все необходимые поля, что значения в полях соответствуют определенным ограничениям (например, целочисленные значения больше или меньше определенного значения) и т.д.

Кроме того, Pydantic позволяет автоматически генерировать документацию для API на основе определенных моделей данных. Это значительно упрощает процесс создания документации и делает ее более точной и надежной.

В целом, использование Pydantic в FastAPI обеспечивает более безопасный и надежный процесс разработки API, упрощает синтаксический анализ и валидацию данных и автоматически генерирует документацию для API.
