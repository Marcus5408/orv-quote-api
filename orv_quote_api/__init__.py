from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import json

app = Flask(__name__)
api = Api(app)

class Quote(Resource):
    def __init__(self, quote_file) -> None:
        super().__init__()
        with open(quote_file, "r", encoding="utf-8") as f:
            self.quotes = json.load(f)

    def get(self):
        return random.choice(self.quotes), 200
    
    # post method temporarily disabled cause I have no way of testing it right now
    # def post(self, quote:str, author:str):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument("quote")
    #     parser.add_argument("author")
    #     params = parser.parse_args()
    #     quote = {
    #         "quote": params["quote"],
    #         "author": params["author"]
    #     }
    #     self.quotes.append(quote)
    #     return quote, 201

@app.route("/shortquote", methods=["GET"])
def short_quote():
    with open("orv_quote_api\short_quotes.json", "r", encoding="utf-8") as f:
        quotes = json.load(f)
    return random.choice(quotes), 200

@app.route("/longquote", methods=["GET"])
def long_quote():
    with open("orv_quote_api\long_quotes.json", "r", encoding="utf-8") as f:
        quotes = json.load(f)
    return random.choice(quotes), 200

@app.route("/quote", methods=["GET"])
def any_quote():
    quote_file = random.choice(["orv_quote_api\short_quotes.json", "orv_quote_api\long_quotes.json"])
    with open(quote_file, "r", encoding="utf-8") as f:
        quotes = json.load(f)
    return random.choice(quotes), 200

# class for the base url of the api.
@app.route("/", methods=["GET"])
def index():
    return "This API provides a single quote from ORV.", 200

if __name__ == '__main__':
    app.run(debug=True)