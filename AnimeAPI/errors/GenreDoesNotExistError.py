from errors.Error import Error


class GenreDoesNotExistError(Error):
    def __init__(self, message):
        super().__init__(message)
