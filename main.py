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
@app.get("/user")
def user():
    return {"users":
            ["mohit","rohit","nandini"]
            }