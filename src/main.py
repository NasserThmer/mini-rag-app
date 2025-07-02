from fastapi import FastAPI 
from routes import base # Assuming base.py is in the routes directory
from routes import data # Assuming data.py is in the routes directory


app = FastAPI()
app.include_router(base.base_router)
app.include_router(data.data_router)
# app.include_router(base_router)