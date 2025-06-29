from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env")  # Load environment variables from .env file
from routes import base 
# from routes.base import base_router
app = FastAPI()
app.include_router(base.base_router)
# app.include_router(base_router)