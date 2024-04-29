from src.repository.CDNRepository import CDNRepository
from src.models.CDN import CDN
from datetime import datetime
from werkzeug.datastructures.file_storage import FileStorage
import secrets

class CDNService():
    __repository: CDNRepository
    __ALLOWED_EXTENSIONS: any
    __UPLOAD_FOLDER: str
    __nbytes: int

    def __init__(self):
        self.__repository = CDNRepository()
        self.__ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
        self.__UPLOAD_FOLDER = './data/img/'
        self.__nbytes = 16

    def __generate_filename(self, filename: str) -> str:
        return secrets.token_hex(nbytes=self.__nbytes) + \
            '.' + filename.rsplit('.', 1)[1].lower()

    def verify_file(self, filename: str) -> bool:
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in self.__ALLOWED_EXTENSIONS

    def create(self, img: FileStorage) -> str or False:
        name = self.__generate_filename(filename=img.filename)
        try:
            img.save(dst=self.__UPLOAD_FOLDER + name)
            new = CDN(name=name)
            response = self.__repository.create(new=new)
            return new.link
        except Exception as e:
            print(e)
            return False
        
    def read(self, _id, link: str) -> bool:
        pass

    def update(self, _id, link: str) -> bool:
        pass

    def delete(self, _id, link: str) -> bool:
        pass
