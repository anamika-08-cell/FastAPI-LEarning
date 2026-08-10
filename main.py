from fastapi import FastAPI 
from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    name:str = Field(min_length=3, max_length=20)
    age:int = Field(1, ge=18)
    objective:Optional[str] = Field(None,min_length=3, max_length=20)

app = FastAPI()
 # real life example.
@app.post("/create-user")
def create_user(user: User):
    return{
       "msg : User has created."
       "user" : user
    }

