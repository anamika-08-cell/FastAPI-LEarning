from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"HELLO WORLD with fastapi with venv"}