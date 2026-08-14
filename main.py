from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

# users = [ ]

class User(BaseModel):
    name:str
    age:int
    password:str

class ResponseUser(BaseModel):
    name:str
    age:int

@app.get("/users",response_model=ResponseUser) 
def create_users():
    return{
        "name":"A",
        "age":17,
        "password":123456
        
    }   #be careful.
    


        
