from math import e
import string
from flask import *
from more_itertools import adjacent
from mariabd_python import *

app = Flask(__name__)


def most_common(lst):
    return max(set(lst), key=lst.count)

def contains_illegal_characters(string):
    illegal_chars = {' ', ',', '.', '-', '_', ':', ';', '<', '>', '!', '#', '&', '()', '=', '?', '+'}

    return any(char in illegal_chars for char in string)

@app.route("/")
def index():
    adjectives_list = get_adjectives()
    if adjectives_list:
        for element in adjectives_list:
            if isinstance(adjectives_list[element], (int)):
                #INT
                pass
            elif isinstance(adjectives_list[element], str):
                # STRING
                pass
            

    else:
        the_adjective = "Nothing here yet"

    return render_template("index.html", html_adjective_list = adjectives, the_adjective_html = the_adjective)

@app.route('/submit', methods=['POST'])
def handle_data():
    if request.method == 'POST':
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')

        print(f"Received: {first_name}")
        print(f"Received: {last_name}")

        # Return a response using write()
        return f'Data received! Your name is: {first_name} {last_name}'
    
    return redirect(url_for('index'))

@app.route("/", methods=["POST"])
def add():
    adjective = request.form.get('adjective')
    if contains_illegal_characters(adjective) == True:
        return redirect(url_for('index'))

        
    write(adjective.lower())
    adjective_list = get_adjectives()

    print(adjective_list)
    print(f"Added {adjective}")

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)