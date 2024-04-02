# !!START
from flask import Flask, render_template, redirect
from .config import Config
from .tweets import tweets
from random import choice, randint
from app.form.tweet_form import Tweet
from datetime import datetime

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/', methods=["GET"])
def index():
  if len(tweets):
    return render_template("index.html", tweet=choice(tweets))
  else:
    return render_template("index.html")

@app.route('/feed', methods=["GET"])
def get_all_tweets():
  modify_tweets = sorted(tweets, key=lambda x: datetime.strptime(x["date"], "%m/%d/%y"))
  # dateTimeObj = datetime.strptime(dateString, "%m/%d/%y")
  return render_template("feed.html", all_tweets=modify_tweets)

@app.route('/new', methods=["GET", "POST"])
def new_tweet():
  form = Tweet()
  if form.validate_on_submit():
    params = {
      "id": len(tweets) + 1,
      "author": form.data["author"],
      "date": str(datetime.now().date()),
      "tweet": form.data["tweet"],
      "likes": randint(50000, 700000)
    }
    tweets.append(params)
    return redirect("/feed")
  return  render_template("new_tweet.html", form=form)

@app.route('/feed/<int:id>/update', methods=["GET", "POST"])
def update_tweet(id):
  form = Tweet()
  if form.validate_on_submit():
    params = {
      "id": id,
      "author": form.data["author"],
      "date": datetime.now().date(),
      "tweet": form.data["tweet"],
      "likes": randint(50000, 700000)
    }
    print(' ----------- Working')
    idx = [idx for idx, tweet in enumerate(tweets) if tweet["id"] == id][0]
    tweets[idx] = params
    return redirect("/feed")
  curr_tweet = [tweet for tweet in tweets if tweet["id"] == id][0]
  form.process(data=curr_tweet)
  return  render_template("new_tweet.html", id=curr_tweet["id"], form=form)

@app.route('/feed/<int:id>/delete', methods=["GET"])
def delete_tweet(id):
  tweet_to_delete = [tweet for tweet in tweets if tweet["id"] == id][0]
  tweets.remove(tweet_to_delete)
  return redirect("/feed")
# !!END
