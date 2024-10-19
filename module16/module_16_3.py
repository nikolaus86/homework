from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# Изначальный словарь пользователей
users = {'1': 'Имя: Example, возраст: 18'}

# 1. GET запрос для получения всех пользователей
@app.get("/users")
async def get_users():
    return users

# 2. POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[str, Path(min_length=5, max_length=20, title="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, title="Enter age")]
):
    user_id = str(max(map(int, users.keys()), default=0) + 1)  # Получаем новый ID на основе максимального
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

# 3. PUT запрос для обновления существующего пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[str, Path(title="Enter User ID", min_length=1)],
    username: Annotated[str, Path(min_length=5, max_length=20, title="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, title="Enter age")]
):
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} has been updated"
    else:
        return f"User {user_id} not found", 404  # Если пользователь не найден

# 4. DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[str, Path(title="Enter User ID", min_length=1)]
):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    else:
        return f"User {user_id} not found", 404  # Если пользователь не найден
