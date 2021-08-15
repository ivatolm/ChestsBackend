from flask import Flask, request

from main import app


@app.route("/api/index")
def index():
    return "Welcome to the API index page."
