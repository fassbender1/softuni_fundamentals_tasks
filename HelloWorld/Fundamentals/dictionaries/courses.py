courses = {}

while True:
    command = input()
    if command == "end":
        break

    course, student = command.split(" : ")
    if course not in courses.keys():
        courses[course] = []

    courses[course].append(student)


for course_name, student_name in courses.items():
    print(f"{course_name}: {len(student_name)}")
    for student_value in student_name:
        print(f"-- {student_value}")



