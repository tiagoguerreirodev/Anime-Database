from services.PostUserAnimeService import PostUserAnimeService


class PostUserAnimeController():
    async def handle(self, anime: dict):
        post_user_anime_service = PostUserAnimeService()
        response = await post_user_anime_service.execute(anime)
        return response
