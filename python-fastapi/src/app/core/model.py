
from datetime import datetime

from sqlmodel import Field, SQLModel

class ModelBase(SQLModel):
    # The value of id will be None until we save it in the database, and then it will finally have a value.
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)