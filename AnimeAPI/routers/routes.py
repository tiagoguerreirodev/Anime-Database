from fastapi import APIRouter, HTTPException
from controllers.GetAllUserAnimeController import GetAllUserAnimeController

from controllers.GetAnimeController import GetAnimeController
from controllers.GetUserAnimeByTitleController import GetUserAnimeByTitleController
from controllers.DeleteUserAnimeController import DeleteUserAnimeController
from controllers.PostUserAnimeController import PostUserAnimeController

from models.Anime import Anime

router = APIRouter()


@router.get("/anime/", tags=['Anime'])
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


@router.get("/user/anime/", tags=['Anime'])
async def get_all_user_anime():
    get_all_user_anime_controller = GetAllUserAnimeController()
    response = await get_all_user_anime_controller.handle()
    if not response:
        raise HTTPException(404, "Não existem animes no banco de dados")
    return response


@router.get("/user/anime/{title}", tags=['Anime'], response_model=Anime)
async def get_user_anime_by_title(title: str):
    get_user_anime_by_title_controller = GetUserAnimeByTitleController()
    response = await get_user_anime_by_title_controller.handle(title)
    if not response:
        raise HTTPException(
            404, f"Não há nenhum anime com o título '{title}' no banco de dados")
    return response


@router.delete("/user/anime/{title}", tags=['Anime'])
async def delete_user_anime(id: int):
    delete_user_anime_controller = DeleteUserAnimeController()
    response = await delete_user_anime_controller.handle(id)
    if not response:
        raise HTTPException(
            404, f"Não há nenhum anime com o id '{id}' no banco de dados")
    return "Anime deletado com sucesso."


@router.post("/user/anime/", tags=['Anime'], response_model=Anime)
async def post_user_anime(anime: Anime):
    post_user_anime_controller = PostUserAnimeController()
    response = await post_user_anime_controller.handle(anime.dict())
    if not response:
        raise HTTPException(
            400, f"Não foi possível salvar '{anime.title}' no banco de dados.")
    return response
