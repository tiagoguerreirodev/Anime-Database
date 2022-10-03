import requests


class DummyRepository():
    def __init__(self):
        self.url = "https://pokeapi.co/api/v2/pokemon/"

    def get_anime(self, genre: str = None, animeName: str = None, perPage: int = 3, page: int = 1):
        response = requests.get(self.url + 'ditto', verify=False)
        return response.json()
