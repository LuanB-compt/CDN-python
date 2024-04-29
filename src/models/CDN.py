class CDN():
    path: str
    name: str
    link: str
    createAt: str
    
    def __dict__(self) -> dict:
        return {
            'path': self.path,
            'name': self.name,
            'link': self.link
        }
