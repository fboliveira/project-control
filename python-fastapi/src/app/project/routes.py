from fastapi import APIRouter

router = APIRouter()

@router.get('/projets')
def get_all_projects():
    return {"projects" : []}