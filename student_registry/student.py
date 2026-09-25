class Student:
    def __init__(self, name, student_id,course):
        self.name = name
        self.student_id = student_id
        self.course= course


student1 = Student("Winston", 22201, "Actuarial Science")
print(student1.name)