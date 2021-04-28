"""
TODO: this is only for testing without having to run all the local lambda server.
"""
import json
from flask import Flask, request, jsonify

from mockingbird.services.request_manager import handle_request
from mockingbird.services.stub_manager import get_stub, create_stub
from mockingbird.utils.decimal_encoder import DecimalEncoder
from mockingbird.utils.exc import MockingException
from mockingbird.utils.logger import get_logger

app = Flask(__name__)


@app.errorhandler(MockingException)
def handle_error(error):
    return app.response_class(
        response=str(error),
        mimetype='application/json',
        status=error.error_code
    )


@app.route("/mock-it/<namespace>/<path:path>")
def mock_it(namespace, path, *args, **kwargs):
    url = "/%s/%s" % (namespace, path)
    raw_response = handle_request(path=url, method=request.method, headers=None, body=request.json)

    response = app.response_class(
        response=json.dumps(raw_response["body"], cls=DecimalEncoder),
        mimetype='application/json'
    )
    return response, int(raw_response["status"])


@app.route("/__admin/mappings", methods=["POST", "GET"])
@app.route("/__admin/mappings/<stub_id>", methods=["PUT", "GET"])
def create_stub_(stub_id=None, *args, **kwargs):
    LOGGER = get_logger("web_app_admin_mappings")

    def get_data_from_request():
        if not request.json:
            raw_data = request.data.decode()
            return json.loads(raw_data)
        return request.json

    if request.method == "GET":
        # TODO: get all the stubs or a specific one
        stubs = get_stub(stub_id=stub_id)
        response = app.response_class(
            response=json.dumps(stubs, cls=DecimalEncoder),
            mimetype='application/json'
        )
        return response
    elif request.method == "POST":
        try:
            data = request.json or request.data.decode()
            if isinstance(data, str):
                data = json.loads(data)
            new_stub = create_stub(data)
            return jsonify(new_stub), 201
        except Exception as err:
            LOGGER.error(err)
            return str(err), 500
    else:
        return "Uh yeah", 204


@app.route("/__admin/requests", methods=["POST", "GET"])
@app.route("/__admin/requests/count", methods=["PUT", "GET", "POST"])
def get_request_data_(*args, **kwargs):
    data = request.json or request.data.decode()
    if isinstance(data, str):
        data = json.loads(data)
    return "This", 200

if __name__ == "__main__":
    app.run(debug=False)

