from flask import Flask, render_template
from typing import List, Dict, Tuple, Set, Union, Optional
import sqlite3
from sqlite3 import Error, Connection, Cursor

app: Flask = Flask(__name__, template_folder='templates')

def get_student_grade_summary(db_path) -> List[Tuple[str, str, str, str, str]]:
    conn: Connection = sqlite3.connect(db_path)
    cursor: Cursor = conn.cursor()
    cursor.execute("""SELECT s.name as name,
               s.cwid as cwid,
               g.course as course,
               g.grade as "grade",
               i.name as instructor_name
            FROM student s
            LEFT JOIN grade g on s.cwid = g.student_cwid
            LEFT JOIN instructor i on g.instructor_cwid = i.cwid
            ORDER BY s.name, g.grade;""")
    return [(row[0], row[1], row[2], row[3], row[4]) for row
                in cursor.fetchall()]


@app.route('/')
def home() -> str:
    rows = get_student_grade_summary('./db.sqlite')
    return render_template('home.html', 
        title='Stevens Repository',
        rows=rows + rows)


app.run(debug=True, port=4000)
