from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    message = "Hello from python!!!"
    return render_template("index.html", message = message)

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

if __name__ == "__main__":
    app.run(debug=True)