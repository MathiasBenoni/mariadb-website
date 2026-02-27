from flask import Flask, render_template, request, redirect, url_for, flash
from mariadb_python import get_adjectives, write
from word_cloud_python import make_cloud
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import spacy
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-me-in-production")
nlp = spacy.load("en_core_web_sm")

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per minute", "40 per hour"]
)

def contains_illegal_characters(string):
    return not all(char.isalpha() for char in string)

BLOCKED_WORDS = {"no", "not", "the", "a", "an", "yes"}

from langdetect import detect

def is_english(word):
    try:
        return detect(word) == "en"
    except:
        return False

def is_adjective(word):
    if word.lower() in BLOCKED_WORDS:
        return False
    if not is_english(word):
        return False


@app.route("/")
def index():
    adjectives = get_adjectives()

    if adjectives:
        the_adjective = max(adjectives, key=adjectives.get).capitalize()
        make_cloud(adjectives)
    else:
        the_adjective = "Nothing here yet"

    return render_template("index.html",
                           html_adjective_list=adjectives,
                           the_adjective_html=the_adjective)


@app.route("/", methods=["POST"])
@limiter.limit("10 per minute; 40 per hour")
def add():
    adjective = request.form.get("adjective", "").strip()

    if not adjective:
        flash("Please enter a word.", "error")
        return redirect(url_for("index"))

    if contains_illegal_characters(adjective):
        flash(f'"{adjective}" contains invalid characters — letters only please.', "error")
        return redirect(url_for("index"))

    if not is_adjective(adjective):
        flash(f'"{adjective}" doesn\'t seem to be an english adjective. Try something describing the site!', "error")
        return redirect(url_for("index"))

    write(adjective.lower())
    flash(f'"{adjective.capitalize()}" was added — thank you!', "success")
    return redirect(url_for("index"))


@app.errorhandler(429)
def rate_limit_exceeded(e):
    flash("Slow down! You're submitting too fast.", "error")
    return redirect(url_for("index")), 429


if __name__ == "__main__":
    app.run(debug=True)