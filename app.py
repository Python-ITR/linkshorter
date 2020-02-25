from server import Server, Route, Router, Request


def index_view(req: Request):
    print("index_view")


def main():
    router = Router()
    router.add_route(Route(r"^/$", index_view))
    server = Server(router=router)
    server.start_loop()


if __name__ == "__main__":
    main()
