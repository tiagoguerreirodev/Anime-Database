from pydantic import BaseModel


class Anime(BaseModel):
    id: int
    title: str
    description: str
    seasonYear: int
    num_episodes: int
    cover_image_url: str
    average_score: int
    genres: list[str]
