from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Tuple
from database import get_db, execute_query, fetch_one, fetch_all

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TaskInDB(Task):
    id: int

# --- CRUD Operations ---

@app.post("/tasks/", response_model=TaskInDB, status_code=201)
def create_task(task: Task, db_cursor: Tuple = Depends(get_db)):
    db, cursor = db_cursor
    query = "INSERT INTO tasks (title, description, completed) VALUES (%s, %s, %s)"
    values = (task.title, task.description, task.completed)
    execute_query(db, cursor, query, values)
    task_id = cursor.lastrowid
    return TaskInDB(id=task_id, **task.dict())

@app.get("/tasks/", response_model=List[TaskInDB])
def read_tasks(db_cursor: Tuple = Depends(get_db)):
    db, cursor = db_cursor
    query = "SELECT id, title, description, completed FROM tasks"
    cursor.execute(query)
    results = fetch_all(cursor)
    tasks = [TaskInDB(id=row[0], title=row[1], description=row[2], completed=row[3]) for row in results]
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskInDB)
def read_task(task_id: int, db_cursor: Tuple = Depends(get_db)):
    db, cursor = db_cursor
    query = "SELECT id, title, description, completed FROM tasks WHERE id = %s"
    cursor.execute(query, (task_id,))
    result = fetch_one(cursor)
    if result is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskInDB(id=result[0], title=result[1], description=result[2], completed=result[3])

@app.put("/tasks/{task_id}", response_model=TaskInDB)
def update_task(task_id: int, task: Task, db_cursor: Tuple = Depends(get_db)):
    db, cursor = db_cursor
    query = "UPDATE tasks SET title=%s, description=%s, completed=%s WHERE id=%s"
    values = (task.title, task.description, task.completed, task_id)
    execute_query(db, cursor, query, values)
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskInDB(id=task_id, **task.dict())

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db_cursor: Tuple = Depends(get_db)):
    db, cursor = db_cursor
    query = "DELETE FROM tasks WHERE id=%s"
    cursor.execute(query, (task_id,))
    execute_query(db, cursor, query)
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
