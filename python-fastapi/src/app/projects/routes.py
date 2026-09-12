from typing import Annotated

from fastapi import APIRouter, Depends, status
from app.projects.services import ProjectService
from app.projects.model import CreateProject, Project

router = APIRouter()

@router.get('/projects', response_model=list[Project])
def get_all_projects(project_service: Annotated[ProjectService, Depends()]):
    return project_service.get_projects()

@router.post('/projects', response_model=Project, status_code=status.HTTP_201_CREATED)
def create_project(create_project : CreateProject, project_service: Annotated[ProjectService, Depends()]):
    return project_service.create_project(create_project)