from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

todos = [ ]

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

#create todos
@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return{
        "message": "todos",
        "data" : todos
    }

#getting all todos
@app.get("/todos")
def get_todos():
    return todos

# for getting single todo
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error" :"todo id not found!"}

# for update todos
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index]=updated_todo
            return {
              "msg":"data_updated",
              "data":updated_todo
            }
    return { "error":"Todo not found."}

#delete API.
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {
                "msg":"Todo Deleted."
            }
    return {
        "msg":"Todo not found."
    }

# for partially update.
@app.patch("/todos/{todo_id}")
def partially_updated_todo(todo_id:int, p_update:Todo):
    for todo in todos:
        if todo.id == todo_id:
            if p_update.id is not None:
                todo.id = p_update.id
            if p_update.title  is not None:
                todo.title = p_update.title
            if p_update.completed is not None:
                todo.completed = p_update.completed
            return { "msg": "Todo partially Updated."}

    return { "msg": "Todo is not found!"}





    



