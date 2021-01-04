from fastapi import APIRouter
from api_v1 import wc

api_router = APIRouter()

api_router.include_router(wc.router, prefix='/Spark', tags=['spark'])