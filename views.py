import jinja2

from http import HTTPStatus
from server import Request, Response, HtmlResponse, HttpBadRequestException
from services import LinksService
from urllib import parse

with open("./templates/index.html", "r") as f:
    index_template = jinja2.Template(f.read())


def index_handler(req: Request) -> Response:
    res = HtmlResponse()
    links = LinksService.getAllLinks()
    res.body = index_template.render(links=links)
    return res


def create_new_link_handler(req: Request) -> Response:
    if len(req.body) == 0:
        raise HttpBadRequestException()
    body = parse.parse_qs(req.body.decode())
    if not body.get("url", None):
        raise HttpBadRequestException()
    original_url = body.get("url")[0]
    link = LinksService.createNewUrl(original_url)
    # Готовим ответ пользователю
    res = Response(HTTPStatus.TEMPORARY_REDIRECT)
    res.addHeader("Location", "/")
    return res
