#!/usr/bin/env python3
"""
todosWeb Backend - FastAPI Server
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import sqlite3
import os
from datetime import datetime

app = FastAPI(title="todosWeb API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database path
DB_PATH = os.environ.get("DB_PATH", "/home/node/.openclaw/workspace/data/todos.db")

# Models
class Todo(BaseModel):
    id: str
    title: str
    status: str
    priority: Optional[str] = "medium"
    created_at: Optional[int] = None
    updated_at: Optional[int] = None

class TodoCreate(BaseModel):
    title: str
    status: str = "todo"
    priority: str = "medium"

class Stats(BaseModel):
    total: int
    done: int
    todo: int
    in_progress: int
    review: int

# Database helper
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def root():
    return {"message": "todosWeb API", "version": "1.0.0"}

@app.get("/api/todos")
def get_todos():
    """取得所有待辦"""
    conn = get_db()
    cursor = conn.execute(
        "SELECT id, title, status, priority, created_at, updated_at FROM todos ORDER BY created_at DESC"
    )
    todos = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {"success": True, "data": todos}

@app.get("/api/todos/{todo_id}")
def get_todo(todo_id: str):
    """取得單一待辦"""
    conn = get_db()
    cursor = conn.execute(
        "SELECT id, title, status, priority, created_at, updated_at FROM todos WHERE id = ?",
        (todo_id,)
    )
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    return {"success": True, "data": dict(row)}

@app.post("/api/todos")
def create_todo(todo: TodoCreate):
    """新增待辦"""
    import time
    todo_id = f"T{int(time.time() * 1000) % 100000:05d}"
    now = int(time.time())
    
    conn = get_db()
    conn.execute(
        "INSERT INTO todos (id, title, status, priority, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
        (todo_id, todo.title, todo.status, todo.priority, now, now)
    )
    conn.commit()
    conn.close()
    
    return {"success": True, "data": {"id": todo_id}}

@app.put("/api/todos/{todo_id}")
def update_todo(todo_id: str, todo: TodoCreate):
    """更新待辦"""
    import time
    now = int(time.time())
    
    conn = get_db()
    conn.execute(
        "UPDATE todos SET title = ?, status = ?, priority = ?, updated_at = ? WHERE id = ?",
        (todo.title, todo.status, todo.priority, now, todo_id)
    )
    conn.commit()
    conn.close()
    
    return {"success": True, "message": "Updated"}

@app.delete("/api/todos/{todo_id}")
def delete_todo(todo_id: str):
    """刪除待辦"""
    conn = get_db()
    conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    
    return {"success": True, "message": "Deleted"}

@app.get("/api/stats")
def get_stats():
    """取得統計"""
    conn = get_db()
    
    # Total
    total = conn.execute("SELECT COUNT(*) FROM todos").fetchone()[0]
    
    # By status
    done = conn.execute("SELECT COUNT(*) FROM todos WHERE status = 'done'").fetchone()[0]
    todo = conn.execute("SELECT COUNT(*) FROM todos WHERE status = 'todo'").fetchone()[0]
    in_progress = conn.execute("SELECT COUNT(*) FROM todos WHERE status = 'in-progress'").fetchone()[0]
    review = conn.execute("SELECT COUNT(*) FROM todos WHERE status = 'review'").fetchone()[0]
    
    conn.close()
    
    return {
        "success": True,
        "data": {
            "total": total,
            "done": done,
            "todo": todo,
            "in_progress": in_progress,
            "review": review
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
