from fastapi import APIRouter, File
from components import spark_functions

router = APIRouter()

@router.post("/word_count")
async def wc(file: bytes = File(...)):
    data = file.decode('utf-8',errors="ignore")
    return spark_functions.wordcount(data)