from fastapi import FastAPI 
# from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     name:str
#     age:int
#     email:str

# @app.post("/create-user")
# def create_user(user:User):
#     return {
#         "msg": "user created",
#         "user": user
#     }

class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name: str
    age : int
    address: Address

@app.post("/create-user")
def create_user(user:User):
    return user



    



