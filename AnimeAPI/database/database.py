import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://db:27017')

database = client.AnimeDB
anime_collection = database.anime
