from flask import Flask, send_from_directory
from flask_restful import Api
import random
# import requests
import os
import json

app = Flask(__name__)
# api = Api(app)

with open('quotes/long_quotes.json', 'r', encoding='utf-8') as f:
    long_quotes = json.load(f)

with open('quotes/short_quotes.json', 'r', encoding='utf-8') as f:
    short_quotes = json.load(f)

@app.route("/shortquote", methods=["GET"])
def short_quote() -> str:
    return random.choice(short_quotes), 200

@app.route("/longquote", methods=["GET"])
def long_quote() -> str:
    return random.choice(long_quotes), 200

@app.route("/quote", methods=["GET"])
def any_quote() -> str:
    quote_file = random.choice([short_quotes, long_quotes])
    return random.choice(quote_file), 200

@app.route("/", methods=["GET"])
def index():
    return "<html><h1>ORV Quote API</h1><p>This API provides a random quote from ORV.</p></html>", 200

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'assets'),
        'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=False)