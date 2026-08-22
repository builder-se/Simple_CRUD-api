import os
from typing import Optional

import psycopg
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

SEED_TASKS = [
    ("Learn FastAPI", False),
    ("Build CRUD API", False),
    ("Write tests", False),
]


def get_connection() -> psycopg.Connection:
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL environment variable is not set")

    return psycopg.connect(DATABASE_URL)


def _row_to_task(row) -> dict:
    return {
        "id": row[0],
        "title": row[1],
        "done": bool(row[2]),
    }


def init_db() -> None:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    done BOOLEAN NOT NULL
                )
                """
            )

            cursor.execute("SELECT COUNT(*) FROM tasks")
            row_count = cursor.fetchone()[0]

            if row_count == 0:
                cursor.executemany(
                    "INSERT INTO tasks (title, done) VALUES (%s, %s)",
                    SEED_TASKS,
                )


def list_tasks() -> list[dict]:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, title, done FROM tasks ORDER BY id")
            rows = cursor.fetchall()

    return [_row_to_task(row) for row in rows]


def get_task_by_id(task_id: int) -> Optional[dict]:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, title, done FROM tasks WHERE id = %s",
                (task_id,),
            )
            row = cursor.fetchone()

    if row is None:
        return None

    return _row_to_task(row)


def create_task(title: str) -> dict:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO tasks (title, done) VALUES (%s, %s) RETURNING id, title, done",
                (title, False),
            )
            row = cursor.fetchone()

    return _row_to_task(row)


def update_task_by_id(task_id: int, title: Optional[str], done: Optional[bool]) -> Optional[dict]:
    existing_task = get_task_by_id(task_id)

    if existing_task is None:
        return None

    updated_title = title if title is not None else existing_task["title"]
    updated_done = done if done is not None else existing_task["done"]

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE tasks
                SET title = %s, done = %s
                WHERE id = %s
                RETURNING id, title, done
                """,
                (updated_title, updated_done, task_id),
            )
            row = cursor.fetchone()

    return _row_to_task(row)


def delete_task_by_id(task_id: int) -> bool:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
            return cursor.rowcount > 0
