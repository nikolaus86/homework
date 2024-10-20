from fastapi import FastAPI, HTTPException, Path, Request, Response
from fastapi.responses import HTMLResponse # импортируем HTMLResponse
from pydantic import BaseModel
from typing import List, Union
from fastapi.templating import Jinja2Templates

app = FastAPI()




# Пустой список пользователей
users = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Подключаем шаблоны Jinja2
templates = Jinja2Templates(directory="templates")

# 1. GET запрос для получения всех пользователей (API)
@app.get("/users", response_model=List[User])
async def get_users_api():
    return users

# 2. POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}", response_model=User)
async def create_user(
    username: str = Path(min_length=5, max_length=20, title="Enter username"),
    age: int = Path(ge=18, le=120, title="Enter age")
):
    user_id = len(users) + 1  # Получаем новый ID
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


# 3. GET запрос для получения одного пользователя по ID (API)
@app.get("/users/{user_id}", response_model=User)
async def get_user_api(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


# 4. PUT запрос для обновления существующего пользователя
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(
    user_id: int = Path(title="Enter User ID", gt=0),
    username: str = Path(min_length=5, max_length=20, title="Enter username"),
    age: int = Path(ge=18, le=120, title="Enter age")
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# 5. DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(
    user_id: int = Path(title="Enter User ID", gt=0)
):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# 6. Маршрут для отображения всех пользователей (HTML)
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def get_users_html(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# 7. Маршрут для отображения одного пользователя (HTML)
@app.get("/user/{user_id}", response_class=HTMLResponse, include_in_schema=False)
async def get_user_html(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User not found")