# learnibg about classes
# manually

class Employees:

    def __init__(self, first, last, pay ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

emp_1 = Employees("John", "Doe", 50000)
emp_2 = Employees("Jane", "Smith", 60000)

print(emp_1)
print(emp_2)


emp_1.first = "John"
emp_1.last = "Doe"
emp_1.email = "johndoe@gmail.com"


emp_2.first = "Jane"
emp_2.last = "Smith"                    
emp_2.email = "janesmith@yahoo.com"

print(emp_1.first)
print(emp_2.email)