from flask import Flask, jsonify

from mockingbird.services.request_manager import handle_request
from mockingbird.services.stub_manager import get_stub


app = Flask(__name__)


@app.route("/mock-it/")
def mock_it(*args, **kwargs):
    stubs = get_stub()
    return jsonify(stubs), 200


@app.route("/create-stub", methods=["POST"])
def create_stub(*args, **kwargs):
    return "Created", 201


@app.route("/get-stubs/<stub_id>", methods=["GET"])
def get_stubs(*args, **kwargs):
    return "ok", 200

