from fastapi import FastAPI, HTTPException,Request
from fastapi.responses import JSONResponse
app = FastAPI()
class UserNotFoundException(Exception):
    def __init__(self, name):
        self.name = name
@app.exception_handler(UserNotFoundException)
def user_not_found_exception(request : Request, exc : UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "msg":f"user not found {exc.name}."
        }
    )
@app.get("/create_user")
def create_user(name):
    if name != "mohit":
        raise UserNotFoundException(name)
    return {
        "name":name
    }



    


        
