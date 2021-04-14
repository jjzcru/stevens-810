# Homework 09 
You've been hired by Stevens Institute of Technology to create a data 
repository of courses, students, and instructors.  The system will be used to 
help students track their required courses, the courses they have successfully 
completed, their grades,  GPA, etc.  The system will also be used by faculty
advisors to help students to create study plans.  We will continue to add new 
features to this solution over the coming weeks so you'll want to think 
carefully about a good design and implementation.  

Your assignment this week is to begin to build the framework for your project 
and summarize student and instructor data.  You'll need to download three 
ASCII, tab separated,  data files:

1. **students.txt** 
   - Provides information about each student.
   - Each line has the format: CWID\tName\tMajor (where \t is the <tab> character)

2. **instructors.txt**
   - Provides information about each instructor. 
   - Each line has the format: CWID\tName\tDepartment (where \t is 
     the <tab> character)

3. **grades.txt**: 
   - Specifies the student CWID, course, and grade for that course, and the 
   instructor CWID. 
   - Each line has the format: Student CWID\tCourse\tLetterGrade\tInstructor
     CWID

Your assignment is to read the data from each of the three files and store it 
in a collection of classes that are easy to process to meet the 
following requirements:

- Your solution should allow a single program to create repositories for 
  different sets of data files, e.g. one set of files for Stevens, another for 
  Columbia University, and a third for NYU. Each university will have different 
  directories of data files.   Hint: you should define a class to hold all of 
  the information for a specific university.
- You may hard code the names of each of the required data file names within a 
  directory, e.g. "students.txt", "instructors.txt", and "grades.txt". Your 
  solution should accept the directory path where the three data files exist 
  so you can easily create multiple sets of input files for testing. I'll test 
  your solution against multiple data directories representing different 
  universities so be sure your solution allows me to easily run against 
  multiple data directories.
- Use your file reader  from HW08 to read the students, instructors, and grades 
  files into appropriate data structures or classes.
- Print warning messages if the input file doesn't exist or doesn't meet the 
  expected format. 
- Print warning messages if the grades file includes an unknown instructor or 
  student
- Use PrettyTable to generate and print a summary table of all of the students 
  with their CWID, name, and a sorted list of the courses they've taken (as 
  specified in the grades.txt file).  
- Use PrettyTable to generate and print a summary table of each of the 
  instructors who taught at least one course with their CWID, name, department, 
  the course they've taught, and the number of students in each class. 
- Implement automated tests to verify that the data in the prettytables 
  matches the data from the input data files. 
- You do NOT need to implement automated tests to catch all possible error 
  conditions but your program should print relevant error messages when invalid 
  or missing data is detected.
- Your solution SHOULD print error messages and warnings to the user about 
  inconsistent or bad data, e.g. a data file with the wrong number of fields or 
  a grade for an unknown student or instructor.
  
## Design choice
- The code is split into multiple files for **Student**, **Instructor** 
  and **Grade**. Each module is independent of each other, by looking at the
  import statements you will see that they only use python primitives.
- Each module has a static method called **from_file**, and the job its to 
  provide an accessible way to load information while respecting the 
  encapsulation of the module. Is more of a utility function.
- The **University** class have **instructor**, **grade** and **student** as 
  dependencies, personally I prefer composition to inheritance, that's the 
  reason that I didn't want to create a dependency between grades and student,
  and grades with professor.
- For the *student.py* you will see three classes:
  - **Student** Is just a data object, it doesn't have any methods
  - **GetBy**: This is just to define an enum I created, so I can take 
    advantage of the autocomplete and feels more self documenting than 
    using **str**.
  - **Students**: It uses the repository pattern, the goal of this class is to 
    provide functions that make it easy to manipulate the data on the list. I 
    created a function call **get** that uses the **GetBy** enum to provide 
    different way to request data while being flexible enough to be extended 
    in the future. (Open/Close Principle). The list is private, so it uses 
    methods to request the data.
- For the *instructor.py* you will see three classes:
  - **Instructor** Is just a data object, it doesn't have any methods
  - **GetBy**: This is just to define an enum I created, so i can take 
    advantage of the autocomplete and feels more self documenting than 
    using **str**.
  - **Instructors**: It uses the repository pattern, the goal of this 
    class is to provide functions that make it easy to manipulate the 
    data on the list. I created a function call **get** that uses the 
    **GetBy** enum to provide different way to request data while being 
    flexible enough to be extended in the future. (Open/Close Principle)
    The list is private, so it uses methods to request the data.
- For the *grade.py* you will see three classes:
  - **Grade** Is just a data object, it doesn't have any methods
  - **GetBy**: This is just to define an enum I created, so I can take 
    advantage of the autocomplete and feels more self documenting than 
    using **str**.
  - **Grades**: It uses the repository pattern, the goal of this class is to 
    provide functions that make it easy to manipulate the data on the list. I 
    created a function call **get** that uses the **GetBy** enum to provide 
    different way to request data while being flexible enough to be extended 
    in the future. (Open/Close Principle). The list is private, so it uses 
    methods to request the data.