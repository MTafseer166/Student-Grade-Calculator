Student Grade Calculator

A Python program that calculates a student's total marks, percentage, grade, and pass/fail status. Supports multiple students and reports the highest scorer.

Features
Takes student name and marks for multiple subjects as input
Validates marks (must be a number between 0 and 100)
Calculates total marks and percentage
Assigns a letter grade (A, B, C, D, F) based on percentage
Determines Pass/Fail status
Supports multiple students in one run
Displays the student with the highest percentage at the end
Code organized using functions for each task
Grading Scale
Percentage	Grade
>= 88	A
>= 76	B
>= 64	C
>= 50	D
< 50	F

Passing threshold: 50%

How to Run
Make sure Python is installed on your system.
Open a terminal in this project folder.
Run the script:
   python grade_calculator.py
Enter the number of students, then for each student enter their name and marks for each subject when prompted.
The program will display each student's total, percentage, grade, and result, and finally show the highest scorer among all students.
Functions Used
get_student_data() — collects and validates a student's name and marks
calculate_total(marks) — sums up all subject marks
calculate_percentage(total, num_subjects) — converts total marks into a percentage
determine_grade(percentage) — assigns a letter grade based on percentage
check_pass_fail(percentage) — determines Pass or Fail
Main loop — runs the above for each student and tracks the top scorer
Input Validation
Marks must be between 0 and 100 (re-prompts if out of range)
Non-numeric input is rejected and re-prompted (using try/except)