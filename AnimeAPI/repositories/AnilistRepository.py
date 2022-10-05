from requests import post, Response
from typing import FrozenSet
from utils import build_query

Genres = FrozenSet[str]


class Anilistepository():
    '''
    Classe responsável pela comunicação com a API GraphQL do Anilist.

    ...

    Atributos
    ---------
    url : str
        A url do serviço, no caso a do Anilist.

    Métodos
    -------
    get_anime(genre: str = None, animeName: str = None, perPage: int = 3, page: int = 1):
        Retorna os animes buscados.
    '''

    def __init__(self):
        self.url: str = 'https://graphql.anilist.co'
        self.possible_genres: Genres = frozenset([
            "Action",
            "Adventure",
            "Comedy",
            "Drama",
            "Ecchi",
            "Fantasy",
            "Hentai",
            "Horror",
            "Mahou Shoujo",
            "Mecha",
            "Music",
            "Mystery",
            "Psychological",
            "Romance",
            "Sci-Fi",
            "Slice of Life",
            "Sports",
            "Supernatural",
            "Thriller"
        ])
        self.baseQuery: str = '''
        query ($page: Int, $perPage: Int, $search: String, $genre: String) {
            Page(page: $page, perPage: $perPage) {
                pageInfo {
                    perPage
                    currentPage
                    lastPage
                    hasNextPage
                }
                media (search: $search, genre: $genre) {
                    id
                    genres
                    description(asHtml=false)
                    seasonYear
                    episodes
                    coverImage
                    averageScore
                    title {
                        romaji
                    }
                }
            }
        }
        '''

    # Buscar os animes na API, por gênero ou por nome.
    def get_anime(self, request: dict[str, str | int]) -> Response:
        json = build_query(self.baseQuery, **request)
        response: Response = post(
            url=self.url, json=json, verify=False)
        return response
