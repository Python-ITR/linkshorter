import logging

# Настраиваем логгер
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from server import Route, Router, Server, serve
from views import index_handler, create_new_link_handler


def main():
    router = Router()
    router.add_route(Route(r"^/$", index_handler))
    router.add_route(Route(r"^/create_link$", create_new_link_handler))
    router.add_route(Route(r"^/static", serve("./static", "/static")))
    server = Server(router=router, addr=("localhost", 9999))
    server.start_loop()


if __name__ == "__main__":
    main()
