from typing import Annotated
from fastapi import APIRouter, Depends

from app.tasks.model import Task
from app.tasks.services import TaskService

router = APIRouter()

@router.get('/tasks', response_model=list[Task])
def get_all_tasks(task_service: Annotated[TaskService, Depends()]):
    return task_service.get_tasks()