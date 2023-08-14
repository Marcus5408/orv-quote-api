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

class short_quote(Quote):
    def __init__(self) -> None:
        super().__init__("orv_quote_api\short_quotes.json")

class long_quote(Quote):
    def __init__(self) -> None:
        super().__init__("orv_quote_api\long_quotes.json")

class any_quote(Quote):
    def __init__(self) -> None:
        super().__init__(random.choice(["orv_quote_api\short_quotes.json", "orv_quote_api\long_quotes.json"]))

# class for the base url of the api.
class home(Resource):
    def get(self):
        return "This API provides a single quote from ORV.", 200

api.add_resource(home, "/")
api.add_resource(any_quote, "/quote", "/quote/")
api.add_resource(short_quote, "/shortquote", "/shortquote/")
api.add_resource(long_quote, "/longquote", "/longquote/")

if __name__ == '__main__':
    app.run(debug=True)