import jinja2

from http import HTTPStatus
from server import (
    Request,
    Response,
    HtmlResponse,
    HttpBadRequestException,
    RedirectResponse,
)
from services import LinksService
from urllib import parse

with open("./templates/index.html", "r") as f:
    index_template = jinja2.Template(f.read())


def index_handler(req: Request) -> Response:
    res = HtmlResponse()
    created_link = None
    links = LinksService.getAllLinks()
    if req.qs:  # success=13
        success_ids = parse.parse_qs(req.qs).get("success")
        if success_ids:
            created_link = LinksService.getLinkById(success_ids[0])
    res.body = index_template.render(links=links, created_link=created_link)
    return res


def create_new_link_handler(req: Request) -> Response:
    if len(req.body) == 0:
        raise HttpBadRequestException(path=req.path)
    body = parse.parse_qs(req.body.decode())
    if not body.get("url", None):
        raise HttpBadRequestException(path=req.path)
    original_url = body.get("url")[0]
    created_link_id = LinksService.createNewUrl(original_url)
    return RedirectResponse(f"/?success={created_link_id}")
