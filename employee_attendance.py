## Employee attendance tracker and weekly wage

# dictionary: name of employees and days present in past business week
employees = {
    "Sandra Smith": 5,
    "Mapula Sokhele": 4,
    "Morisson Made":5,
    "Quinton Nyathi":2,
    "Tshepo Mokaone":0,
    "Sally Olivan":1
}
x = employees.items()
print("*********Attendance for week**********")
print(" ")
print(" ")
print(" ")
for employee,days in x:
    if days < 5:
       print (employee,"-attended", days,"days",": therefore missed certain days at work this week") 
    else:
      print (employee,"attended", days,"days",":therefore present all week")   