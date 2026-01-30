from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def handle_data():
    if request.method == 'POST':
        
        first_name = request.form.get('fname')

        print(f"Received: {first_name}")

        # Return a response or redirect to another page
        return f'Data received! Your name is: {first_name}'
    
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
