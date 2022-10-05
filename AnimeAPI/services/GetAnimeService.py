from requests import request
from errors.GenreDoesNotExistError import GenreDoesNotExistError
from repositories.AnilistRepository import Anilistepository
from requests import Response


class GetAnimeService():
    async def execute(self, request: dict[str, str | int]) -> Response:
        anilist_repository = Anilistepository()
        if request['genre'] not in anilist_repository.possible_genres:
            raise GenreDoesNotExistError(
                "Esse gênero não existe ou está escrito errado.")
        response: Response = anilist_repository.get_anime(request)
        return response
