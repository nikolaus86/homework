from fastapi import FastAPI
from routers.task import router as task_router
from routers.user import router as user_router
from backend.db import engine
from models import Task, User

app = FastAPI()

# Создание таблиц в базе данных
Task.__table__.create(bind=engine, checkfirst=True)
User.__table__.create(bind=engine, checkfirst=True)

@app.get("/")
def read_root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)
