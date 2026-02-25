import os
import requests
from flask import Flask, render_template, request, jsonify
from flask_socketio import emit, SocketIO

app = Flask(__name__)
app.config("SECRET_KEY") = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

votes = {"yes":0, "no":0, "maybe":0}

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("submit vote")
def vote(data): 
    selection = data["selection"]
    votes[selection] +=1
    emit("announce vote", {"selection": selection}, broadcast=True)
