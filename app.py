from flask import Flask, render_template, request, jsonify
import os


app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "<h1>Arpan's Flask App 1</h1>"

if __name__ == "__main__":
    app.run()