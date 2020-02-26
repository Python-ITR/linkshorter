class HttpServerException(Exception):
    def __init__(self, msg, *args, status: int, path: str):
        super().__init__(msg, *args)
        self.msg = msg
        self.status = status


class HttpNotFoundException(HttpServerException):
    def __init__(self, msg = None, *args, **kwargs):
        if not msg:
            msg = "Not found. 404"
        super().__init__(msg, *args, **kwargs, status=404)
