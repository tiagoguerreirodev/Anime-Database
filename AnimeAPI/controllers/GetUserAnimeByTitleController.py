from services.GetUserAnimeByTitleService import GetUserAnimeByTitleService


class GetUserAnimeByTitleController():
    async def handle(self, title: str):
        get_user_anime_by_title_service = GetUserAnimeByTitleService()
        response = await get_user_anime_by_title_service.execute(title)
        return response
