from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

users = [ ]

class User(BaseModel):
    id:int
    name:str
    age:int

@app.post("/users") 
def create_users(user:User):
    users.append(user)
    return {
        "msg": "User creaated..",
        "users": users
    }

@app.get("/users")
def get_user():
    return users

@app.put("/users/{user_id}")
def user_update(user_id:int,update_user:User,notify:bool=False):
    if user_id < len(users):
        users[user_id] = update_user
        return {
            "msg": "User Updated"
            ,"user" : update_user
            ,"notify":notify
        }
    return {
        "msg":"user_is not found."
    }
        
#create todos
# @app.post("/todos")
# def create_todo(todo:Todo):
#     todos.append(todo)
#     return{
#         "message": "todos",
#         "data" : todos
#     }

# #getting all todos
# @app.get("/todos")
# def get_todos():
#     return todos

# for getting single todo
# @app.get("/todos/{todo_id}")
# def get_todo(todo_id:int):
#     for todo in todos:
#         if todo.id == todo_id:
#             return todo
#     return {"error" :"todo id not found!"}

# # for update todos
# @app.put("/todos/{todo_id}")
# def update_todo(todo_id:int, updated_todo:Todo):
#     for index,todo in enumerate(todos):
#         if todo.id == todo_id:
#             todos[index]=updated_todo
#             return {
#               "msg":"data_updated",
#               "data":updated_todo
#             }
#     return { "error":"Todo not found."}

# #delete API.
# @app.delete("/todos/{todo_id}")
# def delete_todo(todo_id:int):
#     for index, todo in enumerate(todos):
#         if todo.id == todo_id:
#             todos.pop(index)
#             return {
#                 "msg":"Todo Deleted."
#             }
#     return {
#         "msg":"Todo not found."
#     }

# # for partially update.
# @app.patch("/todos/{todo_id}")
# def partially_updated_todo(todo_id:int, p_update:Todo):
#     for todo in todos:
#         if todo.id == todo_id:
#             if p_update.id is not None:
#                 todo.id = p_update.id
#             if p_update.title  is not None:
#                 todo.title = p_update.title
#             if p_update.completed is not None:
#                 todo.completed = p_update.completed
#             return { "msg": "Todo partially Updated."}

#     return { "msg": "Todo is not found!"}





    



