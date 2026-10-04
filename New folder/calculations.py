def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    total = calculate_total(marks)
    return total / len(marks)


def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"