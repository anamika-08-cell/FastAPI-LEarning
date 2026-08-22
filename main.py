from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(10)
    return {
        "msg":"Async program"
    }


