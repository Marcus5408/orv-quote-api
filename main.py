from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import json
import requests

app = Flask(__name__)
api = Api(app)

long_quotes = requests.get("https://raw.githubusercontent.com/Marcus5408/orv-quote-api/main/quotes/long_quotes.json").json()
short_quotes = requests.get("https://raw.githubusercontent.com/Marcus5408/orv-quote-api/main/quotes/short_quotes.json").json()

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
    return "This API provides a random quote from ORV.", 200

if __name__ == '__main__':
    app.run(debug=False)