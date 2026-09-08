from core.model import ModelBase

class Project(ModelBase):
    __tablename__ = "tb_projects"
    name: str