# celery_app.py
from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "blood_test_app",
    broker="redis://localhost:6379/0",
    backend=redis_url,
    include=["task"]  # Make sure this matches your task filename without .py
)
