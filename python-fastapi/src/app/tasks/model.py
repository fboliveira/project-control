from sqlmodel import Field, Relationship

from app.core.model import ModelBase
from app.projects.model import Project

class Task(ModelBase, table=True):
    __tablename__ = "tb_tasks"
    description: str
    done: bool
    project_id : int | None = Field(default=None, foreign_key="project.id")

    project: Project | None = Relationship(back_populates="tasks")