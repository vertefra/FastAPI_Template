from fastapi import FastAPI

import uvicorn


app = FastAPI()


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)
