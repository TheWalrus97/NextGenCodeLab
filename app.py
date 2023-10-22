from flask import Flask, request, jsonify
import json


app = Flask(__name__)


@app.route('/', methods=['POST'])
def receive_json():
    try:
        data = request.get_json()
        if 'Command' in data and data['Command'] == 'greeting' and 'name' in data:
            name = data['name']
            response = {"Response": f"hello {name}"}
            return jsonify(response, 200)
        else:
            return jsonify({"error": "Incorrect JSON format or missing parameters"}, 403)
    except Exception as e:
        return jsonify({"error": str(e)}, 400)


if __name__ == "__main__":
    app.run(debug=True)