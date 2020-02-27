import logging
import mimetypes
import os

from .exceptions import HttpNotFoundException
from .request import Request
from .response import Response

logger = logging.getLogger(__name__)


def serve(root: str, prefix: str = ""):
    """
    Функция создает новый хендлер
    @arg root - относительный путь до папки со статикой
    """
    abs_root = os.path.abspath(root)
    logger.debug(f"new static handler with root: {abs_root}")

    def handle_static(req: Request):
        logger.debug(f"handle static request; root: {abs_root}; path: {req.path}")
        prepared_req_path = "." + req.path.replace(prefix, "")
        file_path = os.path.join(
            abs_root, prepared_req_path
        )  # путь до статичного файла
        mime, _ = mimetypes.guess_type(file_path)
        if os.access(file_path, os.F_OK | os.R_OK):
            with open(file_path, "rb") as f:
                res = Response()
                res.body = f.read()
                res.addHeader("Content-Type", mime or "unknown")
                return res
        else:
            raise HttpNotFoundException(
                f"File not found; path: {file_path}", path=req.path
            )

    return handle_static
