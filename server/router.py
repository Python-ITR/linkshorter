import re
from .exceptions import HttpNotFoundException, HttpInternalErrorException

from .request import Request


class Route:
    """
    Экземпляр этого класса представляет собой соответствие между шаблоном и view-функцией
    """

    def __init__(self, pattern_str: str, handler):
        self.pattern = re.compile(pattern_str)
        self.handler = handler  # Функция обработчик запроса (view-function)


class Router:
    def __init__(self):
        self.routes = []

    def add_route(self, route: Route):
        self.routes.append(route)

    def process_request(self, req: Request):
        """
        Метод получает запрос и определяет какой обработчик будет вызван
        Возвращает результат вызова обработчика
        """
        try:
            for route in self.routes:
                match = route.pattern.match(req.path)
                if match:
                    return route.handler(req)
        except Exception:
            raise HttpInternalErrorException()
        raise HttpNotFoundException("Not found matched route", path=req.path)
