students = []
subject_to_check = ""

while True:
    student_info = input()

    if ":" not in student_info:
        subject_to_check = student_info
        break
    else:
        name, ID, subject = student_info.split(":")
        students.append({'name': name, 'ID': ID, 'subject': subject})

for student in students:
    if subject_to_check.startswith(student['subject'][0:5]):
        print(f"{student['name']} - {student['ID']}")

