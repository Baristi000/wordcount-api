from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pyspark import SparkContext

from core.config import settings
from api import api_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host = settings.HOST, port = settings.PORT, reload = True)