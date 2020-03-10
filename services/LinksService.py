import random

from typing import List
from connection import connection
from datetime import datetime
from string import ascii_letters


def getRandomString(length=6) -> str:
    return "".join([random.choice(ascii_letters) for i in range(length)])


def tupleToDict(sorted_keys: List[str], values) -> List[dict]:
    """ Функция получает список ключей в том порядке в котором были перечисленны колонки при запросе в базу данных и получает данные из базы(список кортежей) """
    if isinstance(values, tuple):
        values = [values]
    result = []
    for value in values:
        result.append(dict([(key, value[idx]) for idx, key in enumerate(sorted_keys)]))
    return result


class LinksService:
    @staticmethod
    def getAllLinks():
        columns = ["id", "original_url", "code", "created_at"]
        cur = connection.cursor()
        cur.execute(f"SELECT {', '.join(columns)} FROM links;")
        data = cur.fetchall()
        return tupleToDict(columns, data)

    @staticmethod
    def getLinkById(id: str):
        columns = ["id", "original_url", "code", "created_at"]
        cur = connection.cursor()
        cur.execute(f"SELECT {', '.join(columns)} FROM links WHERE id={id};")
        data = cur.fetchall()
        return tupleToDict(columns, data)[0]

    @staticmethod
    def createNewUrl(original_url: str):
        """ Добавить новую запись в таблицу `links`"""
        cur = connection.cursor()
        code = getRandomString()
        now = datetime.now()
        cur.execute(
            "INSERT INTO links (original_url, code, created_at) VALUES (%s, %s, %s) RETURNING id, code",
            (original_url, code, now),
        )
        link_id, link_code = cur.fetchone()
        connection.commit()
        return link_id
