from flask import Flask, render_template, request, jsonify
import os


app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "<h1>Arpan's Flask App 1</h1>"

@app.route("/echo", methods=["POST"])
def echo():
    """
    Expects a JSON body: { "message": "some string" }
    Returns a JSON response echoing back that string.
    """
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' field in JSON body."}), 400
    
    message = data["message"]
    return jsonify({"echoedMessage": message}), 200

if __name__ == "__main__":
    app.run()