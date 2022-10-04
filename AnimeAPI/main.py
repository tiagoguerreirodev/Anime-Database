from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers.GetAnimeController import GetAnimeController

description = """
AnimeAPI é uma API REST que acessa a API GraphQL do [Anilist](https://github.com/AniList/ApiV2-GraphQL-Docs)

## Animes
Com o AnimeAPI, é possível:
* Buscar animes por gênero
* Buscar animes por nome

## Usuários (não implementado)
Como usuário do Anilist, será possível:
* Manipular sua lista de animes
* Adicionar e remover animes da sua lista
"""

tags_metadata = [
    {
        "name": "Anime",
        "description": "Operações envolvendo animes. Buscar na API e salvar, excluir e consultar no banco de dados local."
    }
]

app = FastAPI(
    title="AnimeAPI",
    description=description,
    version="1.0",
    contact={
        "name": "Tiago da Silva Guerreiro",
        "email": "tiago.guerreiro@br.experian.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)

allowed_origins = [
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/anime/", tags=['Anime'])
def get_anime(page: int, name: str = None, genre: str = None, perPage: int = 3):
    get_anime_controller = GetAnimeController()
    request: dict[str, str | int] = {
        "genre": genre,
        "search": name,
        "perPage": perPage,
        "page": page
    }
    response = get_anime_controller.handle(request=request)
    return response
