from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    return render_template('index.html', title='Home page')

if __name__ == "__main__":
    app.run(debug=True)