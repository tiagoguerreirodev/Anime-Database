import motor.motor_asyncio
from os import environ as env


client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://{'db' if env.get('RUNNING_IN_DOCKER') else 'localhost'}:27017")

database = client.AnimeDB
anime_collection = database.anime
