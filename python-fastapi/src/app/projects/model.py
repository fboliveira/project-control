from sqlmodel import Relationship, SQLModel
from app.core.model import ModelBase
from app.tasks.model import Task

class Project(ModelBase, table=True):
    __tablename__ = "tb_projects"
    name: str

    tasks = list["Task"] = Relationship(back_populates="project")

class CreateProject(SQLModel):
    name: str

class UpdateProject(SQLModel):
    id: int
    name: str

class DeleteProject(SQLModel):
    id: int
