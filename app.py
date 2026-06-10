from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return f"Hello {name}"

@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.json

    name = data.get('name')
    college = data.get('college')

    return jsonify({
        "message": "Student Added Successfully"
    })

if __name__ == '__main__':
    app.run(debug=True)