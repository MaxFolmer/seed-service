import os

import psycopg2
from fastapi import FastAPI

# from dotenv import load_dotenv
from config import settings

greeting = settings.greeting

# load_dotenv()

app = FastAPI()

# Приветствие сервис берёт из окружения.
# Нет переменной GREETING — сервис не стартует.
# greeting = os.environ["GREETING"]


@app.get("/")
def read_root():
    return {"message": greeting}



@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/db-check")
def db_check():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])

    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    cursor.close()
    conn.close()

    return {"status": "ok"}