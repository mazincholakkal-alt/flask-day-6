from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
def hello():
    return "Hello Mazin"

@app.route('/student/')
def student():
    return "Welcome Mazin"

if __name__ == '__main__':
    app.run(debug=True)
