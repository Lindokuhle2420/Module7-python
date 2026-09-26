class Student:
    def __init__(self, name, student_number,course):
        self.marks = []
        self.attendance = 0
        self.assignment_deadline = None
        self.name = name
        self.student_number = student_number
        self.course= course

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Student Number: {self.student_number}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Attendance: {self.attendance}")
        print(f"Assignment Deadline: {self.assignment_deadline}")
        


    def add_marks(self, marks):
        self.marks.append(marks)
        return self.marks
        

    def update_attendance(self):
        self.attendance += 1
        return self.attendance


    def student_type(self):
        print("This is a general student")


class full_time_student(Student):
    def student_type(self):
        print("This is a full-time student")


class part_time_student(Student):
    def student_type(self):
        print("This is a part-time student")
    




 