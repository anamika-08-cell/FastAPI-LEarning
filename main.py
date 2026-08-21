from sqlalchemy import create_engine, Column,Integer,String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends

app = FastAPI()

#database file kaha banegi use batane ke liye.
DATABASE_URL = "sqlite:///./test.db"

#db connect kia.
engine = create_engine(
    DATABASE_URL,
    connect_args = {
        "check_same_thread":False
    }
)

#session actual data type hai.
#db ke through operation kr sakte ho. har ek request ke liye session create krta hai.
sessionLocal = sessionmaker(bind=engine)
#base model.
Base = declarative_base()

#create model class.
class Todo(Base):
    __tablename__= "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)

#fastapi ko db se connect karte hai database session hai ye.
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

#create post api.
@app.post("/todos")
def create_todo(title:str,db:Session=Depends(get_db)):
    todo = Todo(title=title,completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
       "message":"Todo Created",
       "data": todo 
    }