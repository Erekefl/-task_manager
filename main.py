from fastapi import FastAPI
from app.api import user
from app.api import task

app = FastAPI()
app.include_router(user.router)
app.include_router(task.router)
