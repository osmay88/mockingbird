import json
from flask import Flask, request, jsonify

from mockingbird.services.request_manager import handle_request
from mockingbird.services.stub_manager import get_stub, create_stub
from mockingbird.utils.decimal_encoder import DecimalEncoder

app = Flask(__name__)


@app.route("/mock-it/<namespace>/<path:path>")
def mock_it(namespace, path, *args, **kwargs):
    return "You made it", 200


@app.route("/__admin/mappings", methods=["POST", "GET"])
@app.route("/__admin/mappings/<stub_id>", methods=["POST", "GET"])
def create_stub_(stub_id=None, *args, **kwargs):
    if request.method == "GET":
        # TODO: get all the stubs or a specific one
        stubs = get_stub(stub_id=stub_id)
        response = app.response_class(
            response=json.dumps(stubs, cls=DecimalEncoder),
            mimetype='application/json'
        )
        return response
    elif request.method == "POST":
        data = request.json
        new_stub = create_stub(data)
        return jsonify(new_stub,  cls=DecimalEncoder), 201
    else:
        return "Uh yeah", 204


if __name__ == "__main__":
    app.run(debug=True)

