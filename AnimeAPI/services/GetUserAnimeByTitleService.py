from repositories.AnimeDBRepository import AnimeDBRepository


class GetUserAnimeByTitleService():
    async def execute(self, title: str):
        anime_db_repository = AnimeDBRepository()
        response = await anime_db_repository.get_anime_by_title(title)
        return response
