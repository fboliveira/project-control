from app.core.model import ModelBase
from sqlmodel import SQLModel

class Project(ModelBase, table=True):
    __tablename__ = "tb_projects"
    name: str

class CreateProject(SQLModel):
    name: str