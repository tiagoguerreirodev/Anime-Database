from services.DeleteUserAnimeService import DeleteUserAnimeService


class DeleteUserAnimeController():
    async def handle(self, id: int):
        delete_user_anime_service = DeleteUserAnimeService()
        response = await delete_user_anime_service.execute(id)
        return response
