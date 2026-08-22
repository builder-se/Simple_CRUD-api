from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel, Field
from typing import Optional

from app.database import (
    create_task as create_task_record,
    delete_task_by_id,
    get_task_by_id,
    init_db,
    list_tasks,
    update_task_by_id,
)

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
        description="A small CRUD API backed by PostgreSQL for learning FastAPI request handling, validation, and REST patterns.",
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


# Request model for creating a task.
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Learn FastAPI"
            }
        }


# Request model for updating a task.
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
    description="Returns every task currently stored in PostgreSQL.",
)
def get_tasks():
    return {"tasks": list_tasks()}


@app.get(
    "/tasks/{task_id}",
    summary="Get task by ID",
    description="Returns a single task when the ID exists, or 404 when the task is missing.",
    responses={404: {"description": "Task not found"}},
)
def get_task(task_id: int):
    task = get_task_by_id(task_id)

    if task is not None:
        return task

    return JSONResponse(status_code=404, content={"error": "Task not found"})


@app.post(
    "/tasks",
    status_code=status.HTTP_201_CREATED,
    summary="Create a task",
    description="Creates a new task from JSON input, validates the title, and stores it in PostgreSQL.",
    responses={400: {"description": "Invalid task data"}},
)
def create_task(task_data: TaskCreate):
    return create_task_record(task_data.title)

@app.put(
    "/tasks/{task_id}",
    summary="Update a task",
    description="Updates the title and/or done state of an existing task in PostgreSQL.",
    responses={400: {"description": "Invalid task data"}, 404: {"description": "Task not found"}},
)
def update_task(task_id: int, task_data: TaskUpdate):
    task = update_task_by_id(task_id, task_data.title, task_data.done)

    if task is None:
        return JSONResponse(status_code=404, content={"error": "Task not found"})

    return task


@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a task",
    description="Removes a task from PostgreSQL and returns 204 No Content when successful.",
    responses={404: {"description": "Task not found"}},
)
def delete_task(task_id: int):
    deleted = delete_task_by_id(task_id)

    if not deleted:
        return JSONResponse(status_code=404, content={"error": "Task not found"})

    return Response(status_code=status.HTTP_204_NO_CONTENT)
