from fastapi import APIRouter

router = APIRouter()

@router.get('/projects')
def get_all_projects():
    return {"projects" : []}