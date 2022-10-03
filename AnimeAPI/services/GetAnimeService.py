from requests import request
from errors.GenreDoesNotExistError import GenreDoesNotExistError
from errors.NoSearchArgumentsError import NoSearchArgumentsError
from repositories.AnimeDBRepository import AnimeDBRepository
from requests import Response


class GetAnimeService():
    def execute(self, request: dict[str, str | int]) -> Response:
        anime_db_repository = AnimeDBRepository()
        if request['genre'] not in anime_db_repository.possible_genres:
            raise GenreDoesNotExistError(
                "Esse gênero não existe ou está escrito errado.")
        response: Response = anime_db_repository.get_anime(request)
        return response
