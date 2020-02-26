from typing import Union


class Response:
    def __init__(self, status=200, headers={}, body=b""):
        self._status = status
        self._body = body  # type: Union[bytes, str]
        self._headers = headers

    def setStatus(self, status: int):
        """ Установить статус """
        self._status = status

    def addHeader(self, key, value):
        """ Добавить новый заголовок """
        self._headers[key] = value

    def delHeader(self, key):
        """ Удалить заголовок из объекта ответа """
        del self._headers[key]

    def setBody(self, body):
        """ Установить тело ответа (может быть строкой или bytes) """
        self._body = body
        self._updateContentLength()

    def _updateContentLength(self):
        """
        Метод будет добавлять заголовок 'Content-Length' определяя длину self._body
        """
        self.addHeader(
            "Content-Length",
            len(self._body.encode() if type(self._body) == str else self._body),
        )

    def _getHeaders(self) -> str:
        """
        Сформировать строку содержащую:
        - стартовая строка HTTP ответа
        - заголовки
        """
        http_headers_string = f"HTTP/1.1 {self._status} OK\n"
        for key, value in self._headers.items():
            http_headers_string += f"{key}: {value}\n"
        return http_headers_string

    def encode(self) -> bytes:
        """
        Переводит объект ответа в bytes для передачи по сети
        """
        self._updateContentLength()
        http_response_bytes = self._getHeaders().encode()
        if self._body:
            http_response_bytes += b"\r\n"
            http_response_bytes += (
                #      👇 - в случае когда self.body – строка
                self._body.encode()
                if isinstance(self._body, str)
                #      👇 - self.body – bytes
                else self._body
            )
        return http_response_bytes


class TextResponse(Response):
    """ Класс для ответа с Content-Type 'text/plain' """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.addHeader("Content-Type", "text/plain; charset=UTF-8")


class HtmlResponse(Response):
    """ Класс для ответа с Content-Type 'text/html' """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.addHeader("Content-Type", "text/html; charset=UTF-8")


class JsonResponse(Response):
    """ Класс для ответа с Content-Type 'application/json' """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.addHeader("Content-Type", "application/json; charset=UTF-8")
