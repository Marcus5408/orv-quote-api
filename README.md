# Omniscient Reader's Viewpoint Quotes API

This is a simple API that returns a random quote from the book Omniscient Reader's Viewpoint.

## Usage

Send a HTTP `GET` request to `https://orv-quote-api.uk.r.appspot.com` with one of the following endpoints:

- `/` - Basic information about the API.
- `/quote` - Returns a random quote, regardless of size.
- `/shortquote` - Returns a random quote that is less than 100 characters long.
- `/longquote` - Returns a random quote that is more than 100 characters long.

Example usage in Python:

```py
import requests
import json

# get json response from api
response = requests.get("https://orv-quote-api.uk.r.appspot.com/quote").json()

# print the quote
print(f"\"{response['quote']}\"\n - {response['author']}")
```

```bash
$ python example.py
"Get lost, Kim Dokja."
 - Yoo Joonghyuk
```
