
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, select

from app.core.database import get_db_session
from app.tasks.model import Task

SessionDep = Annotated[Session, Depends(get_db_session)]

class TaskService:

    def __init__(self, session : SessionDep):
        self.session = session

    def get_tasks(self) -> list[Task]:
        tasks = self.session.exec(select(Task)).all()
        return tasks