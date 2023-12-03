import uvicorn
from fastapi import FastAPI
from app.infra.web.router import setup_routers
from app.infra.db.database import create_tables

app = FastAPI()
setup_routers(app)


@app.on_event("startup")
async def startup():
    create_tables()


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
