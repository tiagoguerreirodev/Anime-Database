from repositories.AnimeDBRepository import AnimeDBRepository
from fastapi import HTTPException


class PostUserAnimeService():
    async def execute(self, anime: dict):
        anime_db_repository = AnimeDBRepository()
        anime_already_exists = await anime_db_repository.get_anime_by_title(
            anime['title'])
        if anime_already_exists:
            raise HTTPException(409, f"O anime {anime['title']} já existe.")
        response = await anime_db_repository.post_anime(anime)
        if not response:
            raise HTTPException(
                400, f"Não foi possível salvar '{anime.title}' no banco de dados.")
        return response
