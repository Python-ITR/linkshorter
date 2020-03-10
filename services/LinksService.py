import random

from connection import connection
from datetime import datetime
from string import ascii_letters


def getRandomString(length=6) -> str:
    return "".join([random.choice(ascii_letters) for i in range(length)])


class LinksService:
    @staticmethod
    def getAllLinks():
        cur = connection.cursor()
        cur.execute("SELECT id, original_url, code, created_at from links;")
        data = cur.fetchall()
        return [
            {"id": v[0], "original_url": v[1], "code": v[2], "created_at": v[3]}
            for v in data
        ]

    @staticmethod
    def getLinkByCode(code: str):
        pass

    @staticmethod
    def createNewUrl(original_url: str):
        """ Добавить новую запись в таблицу `links`"""
        cur = connection.cursor()
        code = getRandomString()
        now = datetime.now()
        cur.execute(
            "INSERT INTO links (original_url, code, created_at) VALUES (%s, %s, %s)",
            (original_url, code, now),
        )
        connection.commit()
