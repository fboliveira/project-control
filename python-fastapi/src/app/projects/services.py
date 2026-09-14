from datetime import datetime
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, select

from app.core.database import get_db_session

from app.projects.model import CreateProject, DeleteProject, Project, UpdateProject

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

    def update_project(self, update_project : UpdateProject) -> Project:

        statement = select(Project).where(Project.id == update_project.id)
        results = self.session.exec(statement)

        project = results.one()

        print("Original project: ", project)

        project.name = update_project.name
        project.updated_at = datetime.now()

        self.session.commit()
        self.session.refresh(project)

        print("Project after update: ", project)
        return project

    def delete_project(self, delete_project : DeleteProject) -> None:

        statement = select(Project).where(Project.id == delete_project.id)
        results = self.session.exec(statement)

        project = results.one()

        print("Original project: ", project)

        self.session.delete(project)        
        self.session.commit()
