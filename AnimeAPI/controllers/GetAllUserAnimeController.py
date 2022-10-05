from services.GetAllUserAnimeService import GetAllUserAnimeService


class GetAllUserAnimeController():
    async def handle(self):
        get_all_user_animes_service = GetAllUserAnimeService()
        response = await get_all_user_animes_service.execute()
        return response
