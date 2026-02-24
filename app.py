from pickle import NONE
from flask import *
from mariabd_python import *
from word_cloud_python import make_cloud
app = Flask(__name__)


def most_common(lst):
    return max(set(lst), key=lst.count)

def contains_illegal_characters(string):
    illegal_chars = {' ', ',', '.', '-', '_', ':', ';', '<', '>', '!', '#', '&', '()', '=', '?', '+', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

    return any(char in illegal_chars for char in string)

@app.route("/")
def index():
    bigger_number = 0
    max_index = 0
    adjectives_list = get_adjectives()
    
    if adjectives_list:
        for i in range(len(adjectives_list)):
            if isinstance(adjectives_list[i], int):
                # INT
                if adjectives_list[i] > bigger_number:
                    bigger_number = adjectives_list[i]
                    max_index = i 
        the_adjective = adjectives_list[max_index - 1].capitalize()
        
        make_cloud(adjectives_list)

    else:
        the_adjective = "Nothing here yet"
  
    

    return render_template("index.html", html_adjective_list=adjectives_list, the_adjective_html=the_adjective)

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