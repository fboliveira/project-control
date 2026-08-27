from fastapi import FastAPI
from app.project import routes

from app.core.config import Config

config = Config()

app = FastAPI(title=config.APP_NAME)
app.include_router(routes.router)

