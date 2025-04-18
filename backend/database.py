from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
from asyncio import run
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI","") #load from .env file
client = AsyncIOMotorClient(MONGO_URI)
db = client["url_shortener_db"]

# Create an index for 'shortCode' synchronously
async def create_indexes():
    db["urls"].create_index([("shortCode", ASCENDING)], unique=True)


