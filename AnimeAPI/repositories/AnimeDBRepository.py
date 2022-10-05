from database.database import anime_collection
from models.Anime import Anime


class AnimeDBRepository():
    async def get_anime_by_title(self, title: str):
        document = await anime_collection.find_one({
            "title": title
        })
        return document

    async def get_all_animes(self):
        animes = []
        cursor = anime_collection.find({})
        async for document in cursor:
            animes.append(Anime(**document))
        return animes

    async def post_anime(self, anime: dict):
        document = anime
        result = await anime_collection.insert_one(document)
        return document

    async def delete_anime(self, id: int):
        result = await anime_collection.delete_one({"id": id})
        return result
