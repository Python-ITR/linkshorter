import logging

from server import HtmlResponse, Request, Response, Route, Router, Server, serve

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def index_view_v2(req: Request) -> Response:
    res = HtmlResponse()
    with open("./static/index.html", "rb") as f:
        res.setBody(f.read())
    return res


def main():
    router = Router()
    router.add_route(Route(r"^/$", index_view_v2))
    router.add_route(Route(r"^/static", serve("./static", "/static")))
    server = Server(router=router, addr=("localhost", 9999))
    server.start_loop()


if __name__ == "__main__":
    main()
