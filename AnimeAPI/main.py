from fastapi import FastAPI

from controllers.GetAnimeController import GetAnimeController

app = FastAPI()


@app.get("/anime/")
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
