from fastapi import FastAPI ,status, HTTPException

app = FastAPI()

@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user():
    return{
        "User has Created!!"
    }

@app.get("/create-users")
def create_users():

    return{
        "status": 200,
        "msg":"user fetched",
        "data":{
            "name":"mohit",
            "age":15
        }
    }

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code = 404,
            detail = "user has not fetched successfully."
        )
    return {
        "id" : 1,
        "name" :"mohit",
        "age": 10

    }
            
        
    


        
