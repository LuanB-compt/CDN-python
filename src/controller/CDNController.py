import flask
from src.service.CDNService import CDNService
from werkzeug.datastructures.file_storage import FileStorage

bp = flask.Blueprint(name="CDN", import_name=__name__)
service = CDNService()

@bp.route("/", methods=["POST"])
def create():
    if 'file' not in flask.request.files:
        return {}, 400
    img: FileStorage = flask.request.files['file']
    if img.filename == '':
        return {}, 400
    if img and service.verify_file(img.filename):
        response = service.create(img)
        if(response != False):
            return {"link": response}, 200
        else:
            return {}, 500
