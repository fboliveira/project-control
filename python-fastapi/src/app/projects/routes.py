from typing import Annotated

from fastapi import APIRouter, Depends
from app.projects.services import ProjectService

router = APIRouter()

@router.get('/projects')
def get_all_projects(project_service: Annotated[ProjectService, Depends()]):
    project_service.get_projects()