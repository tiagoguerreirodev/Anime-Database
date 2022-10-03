from errors.Error import Error


class NoSearchArgumentsError(Error):
    def __init__(self, message):
        super().__init__(message)
