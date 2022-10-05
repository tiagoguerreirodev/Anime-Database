from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from routers.routes import router

description = """
AnimeAPI é uma API REST que acessa a API GraphQL do [Anilist](https://github.com/AniList/ApiV2-GraphQL-Docs)

## Animes
Com o AnimeAPI, é possível:
* Buscar animes por gênero
* Buscar animes por nome
* Guardar os animes em um banco de dados local

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

allowed_origins = [
    "http://localhost"
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

app.include_router(router)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=allowed_origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=5000)
