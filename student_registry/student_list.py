class student_list:
    def __init__(self):
        self.student_list = []

    def add_student(self,student):
        self.student_list.append(student)
        return self.student_list

    def display_students(self,student_list):
        for student in student_list:
            student.display_student_info()

    def find_student(self, student_list, student):
        for s in student_list:
            if s == student:
                return s
        return None
    