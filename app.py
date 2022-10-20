import requests
from os import environ
from flask import Flask, render_template, url_for
from flask import request as req

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/summary", methods=["GET", "POST"])
def summary():
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {
            "Authorization": f"Bearer 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"}
        data = req.form["data"]
        maxlength = int(req.form["maxlength"])
        minlength = maxlength//4

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        output = query({
            "inputs": data,
            "parameters": {"min_length": minlength, "max_length": maxlength},
        })[0]
        return render_template("index.html", result=output["summary_text"])
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
