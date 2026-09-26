from student  import Student, full_time_student, part_time_student
from student_list import student_list
from storage import save_students, load_students, delete_student_record
from utils import get_deadline, check_deadline

student_list = student_list()
def register_students():
    name = input("Enter student name: ")
    student_number = int(input("Enter student number: "))
    course = input("Enter student course: ")
    print("Select student type:")
    print("1. Full-time student")
    print("2. Part-time student")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        student = full_time_student(name, student_number, course)
    elif choice == 2:
        student = part_time_student(name, student_number, course)
    else:
        student = Student(name, student_number, course)

    return student



def view_student_details(student_number):
    student = find_student(student_list.student_list, student_number)
    if student:
        student.display_student_info()
    else:
        print("Student not found.")

def add_marks(student_number, marks):
    student = find_student(student_list.student_list, student_number)
    if student:
        student.add_marks(marks)
        print("Marks added successfully.")
    else:
        print("Student not found.")

def record_attendance(student_number):
    student = find_student(student_list.student_list, student_number)
    if student:
        student.update_attendance()
        print("Attendance recorded successfully.")
    else:
        print("Student not found.")



print("======SMART STUDENT MANAGEMENT SYSTEM=======")
while True:
    print("\n1. Register Student")
    print("2. View Students")
    print("3. View Student Details")
    print("4. Add Marks")
    print("5. Record Attendance")
    print("6. Set Assignment Deadline")
    print("7. Save Students")
    print("8. Delete Students")
    print("9. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        student = register_students()
        student_list.add_student(student)
    elif choice == 2:
        student_list.display_students(student_list.student_list)
    elif choice == 3:
        student_number = int(input("Enter student number: "))
        view_student_details(student_number)
    elif choice == 4:
        student_number = int(input("Enter student number: "))
        marks = float(input("Enter marks: "))
        add_marks(student_number, marks)
    elif choice == 5:
        student_number = int(input("Enter student number: "))
        record_attendance(student_number)
    elif choice == 6:
        deadline = get_deadline()
        check_deadline(deadline)
    elif choice == 7:
        save_students(student_list)
    elif choice == 8:
        student_number = int(input("Enter student number: "))
        delete_student_record(student_list, student_number)
    elif choice == 9:
        break
    else:
        print("Invalid choice.")