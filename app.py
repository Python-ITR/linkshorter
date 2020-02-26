import logging
from server import Server, Route, Router, Request, TextResponse, Response

logging.basicConfig(level=logging.DEBUG)


def index_view(req: Request) -> bytes:
    return b"HTTP/1.1 200 OK\r\n\r\nHello!"


def index_view_v2(req: Request) -> Response:
    res = TextResponse()
    res.setBody("ЛHello world!")
    return res


def main():
    router = Router()
    router.add_route(Route(r"^/$", index_view_v2))
    server = Server(router=router, addr=("localhost", 9999))
    server.start_loop()


if __name__ == "__main__":
    main()
