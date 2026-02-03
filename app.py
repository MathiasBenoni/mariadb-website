from flask import *
from mariabd_python import *
app = Flask(__name__)

@app.route("/")
def index():
    write("x")
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def handle_data():
    if request.method == 'POST':
        
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')

        print(f"Received: {first_name}")
        print(f"Received: {last_name}")
        # Return a response or redirect to another page
        return f'Data received! Your name is: {first_name} {last_name}'
    
    return redirect(url_for('index'))


def write(x):
    return f'{x}'

if __name__ == "__main__":
    app.run(debug=True)
