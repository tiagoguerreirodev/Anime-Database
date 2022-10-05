from repositories.AnimeDBRepository import AnimeDBRepository


class DeleteUserAnimeService():
    async def execute(self, id: int):
        anime_db_repository = AnimeDBRepository()
        response = await anime_db_repository.delete_anime(id)
        return response
