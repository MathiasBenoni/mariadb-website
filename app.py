from flask import *
from mariabd_python import *
import mariabd_python

app = Flask(__name__)


@app.route("/")
def index():
   
    adjectives = mariabd_python.get_adjectives()
    return render_template("index.html", html_adjective_list = adjectives)

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

@app.route("/add", methods=["POST"])
def add():
    adjective = request.form.get('adjective')

    mariabd_python.write(adjective)

    adjective_list = get_adjectives()

    print(adjective_list)
    print(f"Added {adjective}")
    return f"Added {adjective}"

if __name__ == "__main__":
    app.run(debug=True)