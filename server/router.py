import re

class Route:
    def __init__(self, pattern_str: str, handler):
        self.pattern = re.compile(pattern_str)
        self.handler = handler


class Router:
    def __init__(self):
        self.routes = []

    def add_route(self, route: Route):
        self.routes.append(route)

    def process_request(self, request: "Request"):
        """
        Метод получает запрос и определяет какой обработчик будет вызван
        Возвращает результат вызова обработчика
        """
        for route in self.routes:
            match = route.pattern.match(request.path)
            if match:
                return route.handler(request)
