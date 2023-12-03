from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DB = os.getenv("MONGO_DB")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")


def initialize_db():
    connect(
        db=MONGO_DB,
        username=MONGO_USERNAME,
        password=MONGO_PASSWORD,
        host=MONGO_HOST,
        port=MONGO_PORT,
        uuidRepresentation="standard",  # Adding this line
    )
