"""Python flask implementation to display student information from the database using Python Flask and Jinja2"""
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/instructors')
def inst_summary():
    """inst_summary pulls data from the database link provided and using sql query, the data is passed on the html table format on the localhost"""
    db_path = "C:/Program Files/JetBrains/DataGrip 2020.1/bin/studentdb.db"
    db = sqlite3.connect(db_path)
    
    query = """SELECT students.Name as Student_Name, students.CWID, grades.Course, grades.Grade, instructors.Name as Instructor_Name
                FROM ((students
                INNER JOIN  grades ON students.CWID = grades.StudentCWID)
                INNER JOIN instructors ON grades.InstructorCWID = instructors.CWID) ORDER BY Student_Name ASC;"""
                
    data = [{"Student": Student, "Cwid": Cwid, "Courses": Course, "Grade": Grade, "Instructor": Instructor} for Student, Cwid, Course, Grade, Instructor in db.execute(query)]
    db.close()

    return render_template('instructors.html', 
                            title="Stevens Repository", 
                            table_title="Student, Cwid, Course, Grade & Instructor", 
                            students=data)


app.run(debug=True)