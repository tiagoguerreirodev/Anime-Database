from requests import Response
from services.GetAnimeService import GetAnimeService


class GetAnimeController():
    def handle(self, request: dict[str, str | int]) -> Response:
        get_anime_service = GetAnimeService()
        response: Response = get_anime_service.execute(request)
        return response.json()
