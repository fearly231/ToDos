from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Todo, Base
from pydantic import BaseModel

# tworzymy tabele w bazie
Base.metadata.create_all(bind=engine)

app = FastAPI()

# model wejściowy dla POST
class TodoCreate(BaseModel):
    title: str

# dependency - pobieranie połączenia z bazą
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. Pobranie listy todos
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

# 2. Dodanie todo
@app.post("/todos")
def create_todo(item: TodoCreate, db: Session = Depends(get_db)):
    todo = Todo(title=item.title)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

# 3. Usuwanie todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
        return {"message": "deleted"}
    return {"error": "not found"}
