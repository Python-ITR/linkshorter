from http import HTTPStatus, 

class Response:
    def __init__(self):
        self.status = 200
        self.body = ""
        self.headers = {}

    def setStatus(self, status: int):
        self.status = status

    def encode(self) -> bytes:
        res_str = (
            f"HTTP/1.1 {self.status} OK\n"
        )
        for key, value in self.headers.items():
            res_str += "{key}: {value}\n"
        
        if self.body:
            res_str += "\n"
            res_str += self.body

        return res_str.encode()