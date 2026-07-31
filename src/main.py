import logging
from fastapi import FastAPI
from .routes import router

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Smart Expense Tracker API",
    description="REST API for tracking personal expenses",
    version="1.0.0"
)

app.include_router(router)
