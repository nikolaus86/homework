from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Пустой список пользователей
users = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

@app.on_event("startup")
async def startup_event():
    global users
    users.extend([
        User(id=1, username='UrbanUser', age=24),
        User(id=2, username='UrbanTest', age=22),
        User(id=3, username='Capybara', age=60)
    ])

@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "user_list": users})

@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")

@app.post("/user/{username}/{age}", response_model=User)
async def create_user(
    username: str = Path(min_length=5, max_length=20, title="Enter username"),
    age: int = Path(ge=18, le=120, title="Enter age")
):
    user_id = len(users) + 1  # Получаем новый ID
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

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

@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int = Path(title="Enter User ID", gt=0)):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
