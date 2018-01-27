from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/v1/recommendations", methods=['GET'])
def recommendations():
    list_string = request.args.get("videos")
    list = list_string.split(",")
    return jsonify(list)
