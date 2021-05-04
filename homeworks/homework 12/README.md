# Homework 12

### Author

| Field | Value  |
| ------------- | ------------- |
| **CWID**  | 10467076  |
| **Name**  | Jose  |
| **Last Name**  | Cruz  |

## Getting Started

Run the following command:

```
$ python app.py
```

## Steps

1. Create a directory structure for your solution with a [templates](templates)
   subdirectory, and a base.html template.
2. Define a [query](university.py) using your SQLite database from Homework 11
   that calculates the Student's name, CWID, the name of the course, grade
   earned, and the instructor's name. The example from the lecture may be useful
   for this task.
3. Create a new template [file](base.html) for your new web page. Start by
   understanding how it should look and then perhaps create an HTML with static
   data to test your HTML.
4. Update your static HTML to include Jinja2 variables and statements to use
   data passed with the `render_template()` call.
5. Create a [Flask Python application](app.py) to run your application.
6. Demonstrate that your code works properly by submitting a .zip file with all
   of the files from your solution plus a [screen dump](screenshots) of your
   browser showing the output.
7. Update your GitHub repository to include a new branch with the web solution.

## Query
The query can be found in [university.py](university.py) in the method 
`get_student_grade_summary`. _Line 174_

The query used is the following:
```sqlite
SELECT s.name as name,
    s.cwid as cwid,
    g.course as course,
    g.grade as "grade",
    i.name as instructor_name
FROM student s
    LEFT JOIN grade g on s.cwid = g.student_cwid
    LEFT JOIN instructor i on g.instructor_cwid = i.cwid
    ORDER BY s.name, g.grade;
```
