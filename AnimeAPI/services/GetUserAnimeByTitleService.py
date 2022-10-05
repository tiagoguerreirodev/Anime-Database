from fastapi import HTTPException
from repositories.AnimeDBRepository import AnimeDBRepository


class GetUserAnimeByTitleService():
    async def execute(self, title: str):
        anime_db_repository = AnimeDBRepository()
        response = await anime_db_repository.get_anime_by_title(title)
        if not response:
            raise HTTPException(
                404, f"Não há nenhum anime com o título '{title}' no banco de dados")
        return response
