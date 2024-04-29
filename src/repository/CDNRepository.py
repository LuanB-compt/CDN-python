from bson.objectid import ObjectId
from src.database.MongoDB import mongo_client
from src.models.CDN import CDN


class CDNRepository():

    def create(self, new: CDN) -> str or False:
        try:
            response = mongo_client.db.todos.insert_one(document=new.__dict__())
            return response.inserted_id
        except Exception as e:
            return False

    def read(self, name: str) -> str or False:
        response = mongo_client.db.todos.find_one(filter={"name": name})
        return response['path']

    def update(self, _id, link: str) -> CDN:
        pass

    def delete(self, _id, link: str) -> bool:
        pass
