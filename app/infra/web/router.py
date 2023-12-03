from fastapi import FastAPI
from app.adapters.controllers.member_controller import member_routes


def setup_routers(app: FastAPI):
    app.include_router(member_routes)
