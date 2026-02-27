from flask import *
from mariadb_python import get_adjectives, write
from word_cloud_python import make_cloud
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import spacy

app = Flask(__name__)
app.secret_key = "your_secret_key"  # needed for flash messages
nlp = spacy.load("en_core_web_sm")

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per minute", "40 per hour"]
)

def contains_illegal_characters(string):
    return not all(char.isalpha() for char in string)

BLOCKED_WORDS = {"no", "not", "the", "a", "an", "yes"}

def is_adjective(word):
    if word.lower() in BLOCKED_WORDS:
        return False
        
    sentences = [
        f"This website is so {word}.",
        f"{word}, that is good",
        f"It was very {word}.",
    ]
    for sentence in sentences:
        doc = nlp(sentence)
        for token in doc:
            if token.text == word:
                if token.pos_ in ("ADJ", "ADV"):
                    return True
    return False

@app.route("/")
def index():
    adjectives = get_adjectives()

    if adjectives:
        the_adjective = max(adjectives, key=adjectives.get).capitalize()
        make_cloud(adjectives)
    else:
        the_adjective = "Nothing here yet"

    return render_template("index.html", html_adjective_list=adjectives, the_adjective_html=the_adjective)

@app.route("/", methods=["POST"])
@limiter.limit("10 per minute; 40 per hour")
def add():
    adjective = request.form.get('adjective')

    if not adjective or contains_illegal_characters(adjective):
        flash("Only letters are allowed!", "error")
        return redirect(url_for('index'))
    if not is_adjective(adjective):
        flash(f'"{adjective}" is not an adjective!', "error")
        return redirect(url_for('index'))

    write(adjective.lower())
    flash(f'"{adjective.capitalize()}" has been added!', "success")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)