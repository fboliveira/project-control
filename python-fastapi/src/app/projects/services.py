from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, select

from app.core.database import get_db_session

from app.projects.model import CreateProject, Project

SessionDep = Annotated[Session, Depends(get_db_session)]

class ProjectService:

    def __init__(self, session : SessionDep):
        self.session = session

    def get_projects(self) -> list[Project]:
        projects = self.session.exec(select(Project)).all()
        return projects

    def create_project(self, create_project : CreateProject) -> Project:

        project = Project.model_validate(create_project)

        self.session.add(project)
        self.session.commit()

        self.session.refresh(project)

        return project