import uvicorn
from fastapi import FastAPI
from app.infra.web.router import setup_routers

app = FastAPI()
setup_routers(app)


@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=7070,
        reload=True,
    )
