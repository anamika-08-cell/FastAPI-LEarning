from fastapi import FastAPI , Query
from typing import Optional

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
# @app.get("/user")
# def get_user(name:str=None):
#     return {"name":
#             name
#             }


@app.get("/user")
def get_user_read(item_name:Optional[str]= Query(None, max_length=50, min_length=3)
             ,limit:int=Query(1,ge=1),
              price:int=Query(50,le=1000) ):
    
    return {"limit":
            limit,
            "item_name":
            item_name,
            "price":
            price
            }