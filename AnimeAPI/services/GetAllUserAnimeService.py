from repositories.AnimeDBRepository import AnimeDBRepository


class GetAllUserAnimeService():
    async def execute(self):
        anime_db_repository = AnimeDBRepository()
        response = await anime_db_repository.get_all_animes()
        return response
