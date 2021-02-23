from fastapi import FastAPI

import uvicorn

from config.settings import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    description=settings.DESCRIPTION,
    version=settings.VERSION
)


if __name__ == '__main__':
    uvicorn.run("main:app", host=settings.APP_HOST,
                port=settings.APP_PORT, reload=settings.RELOAD)
