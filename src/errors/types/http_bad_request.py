class HttpBadResquestError(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.nome = 'BadRequest'
        self.status_code = 400
        