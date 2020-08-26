from flask import Flask, render_template, request
import configparser
import requests
import os
from scraper import scraper

app = Flask(__name__)
app.debug = True


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results", methods=["POST"])
def results():
    username = request.form["userName"]
    rankings = scraper.get_playlists(username)
    return render_template("results.html", rankings=rankings)


if __name__ == '__main__':
    app.run()






