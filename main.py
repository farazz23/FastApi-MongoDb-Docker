from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes import route
from database import db_config

connect_to_mongo = db_config.connect_to_mongo
close_connection = db_config.close_connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    connect_to_mongo()
    yield
    # Shutdown
    close_connection()


app = FastAPI()
app.include_router(route.router)

