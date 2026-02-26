from flask import *
from mariadb_python import get_adjectives, write
from word_cloud_python import make_cloud
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per minute", "40 per hour"]
)

def contains_illegal_characters(string):
    return not all(char.isalpha() for char in string)

def is_adjective(word):
    doc = nlp(f"That website is so {word}")
    for token in doc:
        if token.text == word:
            return token.pos_ == "ADJ"
        else:
            doc = nlp(f"This is {word}")
            for token in doc:
                if token.text == word:
                    return token.pos_ == "ADJ"
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
        return redirect(url_for('index'))
    if not is_adjective(adjective):
        return redirect(url_for('index'))

    write(adjective.lower())
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)