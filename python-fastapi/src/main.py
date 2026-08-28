import uvicorn

from fastapi import FastAPI
from app.project import routes

from app.core.config import Config

config = Config()

app = FastAPI(title=config.APP_NAME)
app.include_router(routes.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=config.SERVER_HOST, port=config.SERVER_PORT, reload=True)

