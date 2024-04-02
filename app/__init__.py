# !!START
from flask import Flask, render_template
from .config import Config
from .tweets import tweets
from random import choice

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/', methods=["GET"])
def index():
  return render_template("index.html", tweet=choice(tweets))

@app.route('/feed', methods=["GET"])
def get_all_tweets():
  return render_template("feed.html", all_tweets=tweets)

# !!END
