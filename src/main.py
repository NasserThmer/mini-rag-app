from fastapi  import FastAPI 
from routes import base , data # Assuming base.py is in the routes directory
app = FastAPI()
app.include_router(base.base_router)
app.include_router(data.data_router)
