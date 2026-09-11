def get_student_data():
    name = input("Enter student name:")
    
    num_subjects = int(input("How many subjects? "))
    marks = []                 
    
    for i in range(num_subjects):
        while True:
            try:
                mark = int(input("Enter your marks: "))
                if mark < 0 or mark > 100:
                    print("Invalid marks! Please enter a value between 0 and 100.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number, not text!")
        
        marks.append(mark)
    
    return name, marks

def calculate_total(marks):
    total = sum(marks)       
    return total

def calculate_percentage(total, num_subjects, max_marks_per_subject=100):
    percentage = total / (num_subjects * max_marks_per_subject) * 100 
    return percentage

def determine_grade(percentage):
    if percentage >= 88:
        grade = "A"
    elif percentage >= 76:
        grade = "B"
    elif percentage >= 64:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    
    return grade

def check_pass_fail(percentage):
    if percentage >= 50:
        result = "Pass"
    else:
        result = "Fail"
    
    return result

students_results = []  

num_students = int(input("How many students? "))

for s in range(num_students):
    print(f"\n--- Student {s+1} ---")
    name, marks = get_student_data()
    total = calculate_total(marks)
    percentage = calculate_percentage(total, len(marks))
    grade = determine_grade(percentage)
    result = check_pass_fail(percentage)
    
    print(f"Name: {name}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Result: {result}")
    
    student_record = {
        "name": name,
        "percentage": percentage
    }
    students_results.append(student_record)

top_student = max(students_results, key=lambda student: student["percentage"])

print(f"\nHighest scorer: {top_student['name']} with {top_student['percentage']:.2f}%")