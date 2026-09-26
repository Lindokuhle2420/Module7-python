from datetime import date


def get_deadline(year,month,day):
    return date()


def check_deadline(get_deadline):
    today = date.today()
    if today > deadline:
        return "Assignment is overdue"
    elif today == deadline:
        return "Assignemt is due today"
    else :
        return"Assignment is not yet due" 
