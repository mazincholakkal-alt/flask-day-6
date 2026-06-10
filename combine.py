from flask import Flask, jsonify, request

app = Flask(__name__)

# Route 1: Student Information
@app.route('/student', methods=['GET'])
def student():
    return jsonify({
        "name": "James",
        "age": 20,
        "branch": "Computer Science"
    })

# Route 2: Course Information
@app.route('/course', methods=['GET'])
def course():
    return jsonify({
        "course_name": "Python Full Stack",
        "duration": "6 Months",
        "mode": "Online"
    })

# Route 3: Trainer Information
@app.route('/trainer', methods=['GET'])
def trainer():
    return jsonify({
        "trainer_name": "John",
        "experience": "5 Years",
        "specialization": "Python"
    })

# Route 4: Add Student
@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.json

    name = data.get('name')
    college = data.get('college')

    return jsonify({
        "message": "Student Added Successfully",
        "name": name,
        "college": college
    })

if __name__ == '__main__':
    app.run(debug=True)