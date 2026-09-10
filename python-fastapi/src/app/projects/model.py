from app.core.model import ModelBase

class Project(ModelBase, table=True):
    __tablename__ = "tb_projects"
    name: str