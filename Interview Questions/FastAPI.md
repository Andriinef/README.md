# FastAPI

## Что такое FastAPI?

**FastAPI** — это веб-фреймворк для создания API с Python 3.7+ на основе стандартных аннотаций типов Python.

## Каковы особенности FastAPI?

- Быстро и эффективно

- Легко использовать

- Интуитивно понятные API с использованием подсказок типа Python

- Автоматическая проверка данных, сериализация и документирование

- Поддержка GraphQL включена по умолчанию.

- Встроенная поддержка синтаксиса async/await.

## Какие базы данных поддерживает FastAPI?

FastAPI поддерживает любой сервер базы данных, совместимый с SQLAlchemy ORM, такой как PostgreSQL, MySQL, SQLite и т. д.

## Как установить FastAPI?

Вы можете установить FastAPI через pip | pienv:

```code
pip install fastapi

pipenv install fastapi
```

## Какова цель зависимости в FastAPI?

**Зависимость** — это функция, которая предоставляет определенный ресурс для маршрута.

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

**Pydantic** библиотека проверки данных, которая поддерживает FastAPI.

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

**Фоновая задача** - это функция, которая асинхронно работает с основным приложением.Вы можете использовать метод `founaltasks.add_task`, чтобы добавить фоновую задачу в Fastapi.

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

**Route39** это новая функция, добавленная в Fastapi v0.65.0, которая позволяет вам определять маршруты, используя имя функции вместо аннотации.

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
