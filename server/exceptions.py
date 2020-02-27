from http import HTTPStatus


class HttpServerException(Exception):
    """
    Базовый класс для ошибок сервера
    """

    def __init__(self, msg, status: HTTPStatus, path: str):
        self.msg = msg
        self.status = status  # type: HTTPStatus

    def __str__(self):
        return f"<{self.__class__.__name__} msg='{self.msg}' status='{self.status}'>"


class HttpNotFoundException(HttpServerException):
    def __init__(self, msg=None, *args, **kwargs):
        if not msg:
            msg = HTTPStatus.NOT_FOUND.description
        super().__init__(msg, *args, **kwargs, status=HTTPStatus.NOT_FOUND)


class HttpInternalErrorException(HttpServerException):
    def __init__(self, msg=None, *args, **kwargs):
        if not msg:
            msg = HTTPStatus.INTERNAL_SERVER_ERROR.description
        super().__init__(msg, *args, **kwargs, status=HTTPStatus.INTERNAL_SERVER_ERROR)
