from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel, Field
from typing import Optional

from app.database import get_connection, init_db

app = FastAPI()


@app.on_event("startup")
def startup_event() -> None:
    init_db()


# Custom exception handler to convert 422 validation errors to 400
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """
    Convert Pydantic validation errors (422) to 400 Bad Request.
    This matches FlyRank requirements for API specification.
    """
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": str(exc.errors()[0]["msg"])}
    )


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Task API",
        version="1.0",
        summary="FlyRank CRUD task API",
        description="A small in-memory CRUD API for learning FastAPI request handling, validation, and REST patterns.",
        routes=app.routes,
    )

    for path_item in openapi_schema.get("paths", {}).values():
        for operation in path_item.values():
            if isinstance(operation, dict):
                responses = operation.get("responses")
                if isinstance(responses, dict):
                    responses.pop("422", None)

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


# Pydantic model for creating a task
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Learn FastAPI"
            }
        }


# Pydantic model for updating a task
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    done: Optional[bool] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Updated Task Title",
                "done": True
            }
        }


def _row_to_task(row):
    return {
        "id": row[0],
        "title": row[1],
        "done": bool(row[2]),
    }


@app.get(
    "/",
    summary="API metadata",
    description="Returns the API name, version, and the main task endpoint available in this project.",
)
def read_root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get(
    "/health",
    summary="Health check",
    description="Returns a simple status payload that can be used by monitors and deployment checks.",
)
def health_check():
    return {"status": "ok"}


@app.get(
    "/tasks",
    summary="List tasks",
    description="Returns every task currently stored in SQLite.",
)
def get_tasks():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()

    return {"tasks": [_row_to_task(row) for row in rows]}


@app.get(
    "/tasks/{task_id}",
    summary="Get task by ID",
    description="Returns a single task when the ID exists, or 404 when the task is missing.",
    responses={404: {"description": "Task not found"}},
)
def get_task(task_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()

    if row is not None:
        return _row_to_task(row)

    return JSONResponse(status_code=404, content={"error": "Task not found"})


@app.post(
    "/tasks",
    status_code=status.HTTP_201_CREATED,
    summary="Create a task",
    description="Creates a new task from JSON input, validates the title, assigns the next ID, and stores it in SQLite.",
    responses={400: {"description": "Invalid task data"}},
)
def create_task(task_data: TaskCreate):
    # Store the new task in the SQLite database and return the created row.
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            (task_data.title, False),
        )

        # Commit the change so the row is persisted and lastrowid is available
        conn.commit()

        new_id = cursor.lastrowid

    return {"id": new_id, "title": task_data.title, "done": False}

@app.put(
    "/tasks/{task_id}",
    summary="Update a task",
    description="Updates the title and/or done state of an existing task in SQLite.",
    responses={400: {"description": "Invalid task data"}, 404: {"description": "Task not found"}},
)
def update_task(task_id: int, task_data: TaskUpdate):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT title, done FROM tasks WHERE id = ?",
            (task_id,),
        )
        row = cursor.fetchone()

        if row is None:
            return JSONResponse(status_code=404, content={"error": "Task not found"})

        title = task_data.title if task_data.title is not None else row[0]
        done = task_data.done if task_data.done is not None else bool(row[1])

        cursor.execute(
            "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
            (title, done, task_id),
        )
        conn.commit()

    return {"id": task_id, "title": title, "done": done}


@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a task",
    description="Removes a task from SQLite and returns 204 No Content when successful.",
    responses={404: {"description": "Task not found"}},
)
def delete_task(task_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

        if cursor.rowcount == 0:
            return JSONResponse(status_code=404, content={"error": "Task not found"})

        conn.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)