from flask import Flask, jsonify, request

from mockingbird.services.request_manager import handle_request
from mockingbird.services.stub_manager import get_stub


app = Flask(__name__)


@app.route("/mock-it/<namespace>/<path:path>")
def mock_it(namespace, path, *args, **kwargs):
    return "You made it", 200


@app.route("/__admin/mappings", methods=["POST", "GET"])
def create_stub(*args, **kwargs):
    if request.method == "GET":
        # TODO: get all the stubs or a specific one
        return "NO stubs yet", 200
    elif request.method == "POST":
        return "Your stub was created", 201
    else:
        return "Uh yeah", 204


if __name__ == "__main__":
    app.run()

