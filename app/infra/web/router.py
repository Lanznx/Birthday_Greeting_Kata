from fastapi import FastAPI
from app.adapters.controllers.member_controller import member_routes
from app.adapters.controllers.greeting_controller import greeting_routes


def setup_routers(app: FastAPI):
    app.include_router(member_routes)
    app.include_router(greeting_routes)
