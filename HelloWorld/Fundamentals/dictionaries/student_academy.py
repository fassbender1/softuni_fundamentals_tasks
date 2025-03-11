entries = int(input())
student_grades = {}

for _ in range(entries):
    student = input()
    grade = float(input())
    if student not in student_grades.keys():
        student_grades[student] = [grade]
    else:
        student_grades[student].append(grade)

final_list = {}

for key, value in student_grades.items():
    average = sum(value) / len(value)
    if average < 4.50:
        continue
    else:
        final_list[key] = average

for name, grade in final_list.items():
    print(f"{name} -> {grade :.2f}")


