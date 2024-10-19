from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Пустой список пользователей
users = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# 1. GET запрос для получения всех пользователей
@app.get("/users", response_model=List[User])
async def get_users():
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

# 3. PUT запрос для обновления существующего пользователя
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

# 4. DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(
    user_id: int = Path(title="Enter User ID", gt=0)
):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
