import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    # query the api for currency exchange rate
    currency = request.form.get("currency")
    res = requests.get("https://api.fxratesapi.com/latest", params={"base":"USD", "symbols":currency})

    # make sure request succeeded
    if res.status_code != 200 :
        return jsonify({"success": False})
    
    # make sure currency is in response
    data = res.json()
    if currency not in data["rates"] :
        return jsonify({"success" : False})
    
    return jsonify({"success": True, "rate": data["rates"][currency]})