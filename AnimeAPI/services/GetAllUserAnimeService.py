from fastapi import HTTPException
from repositories.AnimeDBRepository import AnimeDBRepository


class GetAllUserAnimeService():
    async def execute(self):
        anime_db_repository = AnimeDBRepository()
        response = await anime_db_repository.get_all_animes()
        if not response:
            raise HTTPException(404, "Não existem animes no banco de dados")
        return response
