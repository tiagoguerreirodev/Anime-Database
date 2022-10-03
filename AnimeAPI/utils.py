def build_query(query: str, genre: str = None, search: str = None, perPage: int = 3, page: int = 1):
    query_vars = {
        "genre": genre,
        "search": search,
        "perPage": perPage,
        "page": page
    }
    return {
        "query": query,
        "variables": query_vars
    }
