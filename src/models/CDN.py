from datetime import datetime

class CDN():
    path: str
    name: str
    link: str
    createAt: str

    def __init__(self, name: str):
        self.name = name.rsplit(sep='.', maxsplit=1)[0]
        self.path = f'./data/imgs/img_{name}'
        self.link = f'http:localhost:5000/{self.name}'
        self.createAt = datetime.now()

    def __dict__(self) -> dict:
        return {
            'path': self.path,
            'name': self.name,
            'link': self.link,
            'createAt': self.createAt
        }
