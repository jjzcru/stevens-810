"""Flask University

    CONVENTIONS:
        - Max character limit per line 80
        - CapWords for class names
        - snake_case for variables and functions
        - double quotes for strings

   Author: Jose J. Cruz
   CWID: 10467076
"""

from flask import Flask, render_template
from university import University

app: Flask = Flask(__name__, template_folder="templates")


@app.route('/')
def home() -> str:
    # Display the grade summary in a web page
    try:
        db_path: str = "./db.sqlite"
        repository: University = University(db_path)
        rows = repository.get_student_grade_summary()
    except Exception as e:
        return render_template('error.html',
                               title='Stevens Repository',
                               message=str(e))
    else:
        return render_template('home.html',
                               title='Stevens Repository',
                               rows=rows)


app.run(debug=True, port=4000)
