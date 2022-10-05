from fastapi import HTTPException
from repositories.AnimeDBRepository import AnimeDBRepository


class DeleteUserAnimeService():
    async def execute(self, id: int):
        anime_db_repository = AnimeDBRepository()
        response = await anime_db_repository.delete_anime(id)
        if not response:
            raise HTTPException(
                404, f"Não há nenhum anime com o id '{id}' no banco de dados")
        return {
            "message": "Anime deletado com sucesso",
            "response": response.raw_result
        }
