from flask import Flask, render_template, request
from database import create_table, add_student, search_student, get_all_students, delete_student

app = Flask(__name__)

create_table()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    msg = ""

    if request.method == "POST":
        roll = request.form["roll_number"]
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        success = add_student(roll, name, age, course)

        if success:
            msg = "Student added successfully!"
        else:
            msg = "Roll number already exists!"

    return render_template("add_student.html", msg=msg)

@app.route("/search", methods=["GET", "POST"])
def search():
    student = None
    msg = ""

    if request.method == "POST":
        roll = request.form["roll_number"]
        student = search_student(roll)

        if not student:
            msg = "Student not found!"

    return render_template("search.html", student=student, msg=msg)

@app.route("/students")
def students():
    data = get_all_students()
    return render_template("students.html", students=data)

@app.route("/delete/<roll>")
def delete(roll):
    delete_student(roll)
    return render_template("delete_success.html")

if __name__ == "__main__":
    app.run(debug=True)