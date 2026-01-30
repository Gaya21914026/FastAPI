from fastapi import FastAPI
from fastapi import FastAPI
from app.core.pong import router as pong_router
from app.routers.cvs import router as upload_router
from dotenv import load_dotenv


load_dotenv() 

app = FastAPI()
app.include_router(pong_router)
app.include_router(upload_router)