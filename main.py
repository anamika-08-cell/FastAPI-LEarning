from fastapi import FastAPI

app = FastAPI()

# home route.
@app.get("/")
def home():
    return {"message":"HELLO WORLD"}

# about route.
@app.get("/about")
def about():
    return {"message":"This is a about page."}

# user route.
@app.get("/user/{user_id}")
def get_user(user_id:int):
    return {"user_id":
            user_id
            }