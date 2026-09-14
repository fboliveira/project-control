from typing import Annotated

from fastapi import APIRouter, Depends, status
from app.projects.services import ProjectService
from app.projects.model import CreateProject, DeleteProject, Project, UpdateProject

router = APIRouter()

@router.get('/projects', response_model=list[Project])
def get_all_projects(project_service: Annotated[ProjectService, Depends()]):
    return project_service.get_projects()

@router.post('/projects', response_model=Project, status_code=status.HTTP_201_CREATED)
def create_project(create_project : CreateProject, project_service: Annotated[ProjectService, Depends()]):
    return project_service.create_project(create_project)

@router.put('/projects', response_model=Project)
def update_project(update_project : UpdateProject, project_service: Annotated[ProjectService, Depends()]):
    return project_service.update_project(update_project)

@router.delete('/projects', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def update_project(delete_project : DeleteProject, project_service: Annotated[ProjectService, Depends()]):
    project_service.delete_project(delete_project)