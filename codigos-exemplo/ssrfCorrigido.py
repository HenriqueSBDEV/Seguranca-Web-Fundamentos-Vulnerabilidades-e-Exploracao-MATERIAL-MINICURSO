from flask import Flask, request
import requests

app = Flask(__name__)

ALLOWED_DOMAINS = [
    "example.com"
]

@app.route("/fetch")
def fetch():

    url = request.args.get("url")

    if "example.com" not in url:
        return "URL não permitida"

    response = requests.get(url)

    return response.text

if __name__ == "__main__":
    app.run(debug=True)