import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/credit/")
async def credit(passport: str, summary: float, percent: float, month: int):
    return {'answer': random.choices(['yes', 'no'], weights=[90, 10], k=1)[0]}
