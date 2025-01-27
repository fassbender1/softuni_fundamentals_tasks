# Напишете програма, която изчислява средната оценка на ученик от цялото му обучение.
# На първия ред ще получите името на ученика, а на всеки следващ ред неговите годишни оценки.
# Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или равна на 4.00.
# Ако ученикът бъде скъсан повече от един път, то той бива изключен и програмата приключва,
# като се отпечатва името на ученика и в кой клас бива изключен.

# При успешно завършване на 12-ти клас да се отпечата :
# "{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"
#
# В случай, че ученикът е изключен от училище, да се отпечата:
# "{име на ученика} has been excluded at {класа, в който е бил изключен} grade"
#
# Стойността трябва да бъде форматирана до втория знак след десетичната запетая.

# student = input()
#
# grade_count = 1
# times_failed = 0
# sum_grades = 0
# average = 0
#
# while times_failed <= 1:
#     annual_grade = float(input())
#     if annual_grade < 4.00:
#         times_failed += 1
#     else:
#         grade_count += 1
#         sum_grades += annual_grade
#         if grade_count > 12:
#             average = sum_grades / (grade_count - 1)
#             break
#
# if grade_count > 12:
#     print(f"{student} graduated. Average grade: {average :.2f}")
# else:
#     print(f"{student} has been excluded at {grade_count} grade")

student = input()

grade_count = 1
times_failed = 0
sum_grades = 0

while True:
    annual_grade = float(input())
    if annual_grade < 4.00:
        times_failed += 1
        if times_failed > 1:
            print(f"{student} has been excluded at {grade_count} grade")
            break
        continue

    sum_grades += annual_grade
    if grade_count == 12:
        print(f"{student} graduated. Average grade: {(sum_grades / grade_count) :.2f}")
        break
    grade_count += 1





