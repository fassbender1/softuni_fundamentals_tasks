def grade(g):
    if 2.00 <= g < 3.00:
        return "Fail"
    elif 3.00 <= g < 3.50:
        return "Poor"
    elif 3.50 <= g < 4.50:
        return "Good"
    elif 4.50 <= g < 5.50:
        return "Very Good"
    elif 5.50 <= g <= 6.00:
        return "Excellent"


student_grade = float(input())
result = grade(student_grade)

print(result)
