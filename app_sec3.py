from flask import Flask, request, jsonify

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "My Item",
                "price": 15.99
            }
        ]
    }
]


@app.route("/store", methods=["GET"])
def get_stores():
    return jsonify({"stores": stores})


@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return jsonify(new_store), 201


@app.route("/store/<string:name>/item", methods=["POST"])
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return jsonify(new_item), 201
    return jsonify({"message": "Store not found"}), 404


@app.route("/store/<string:name>", methods=["GET"])
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "Store not found"}), 404


@app.route("/store/<string:name>/item", methods=["GET"])
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return jsonify({"message": "Store not found"}), 404
