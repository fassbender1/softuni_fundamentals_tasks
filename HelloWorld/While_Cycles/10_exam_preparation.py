# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
# При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда "Enough"
# или ако Марин получи определения брой незадоволителни оценки. Незадоволителна е всяка оценка,
# която е по-малка или равна на 4.
# Вход
# · На първи ред - брой незадоволителни оценки - цяло число;
# · След това многократно се четат по два реда:
# o Име на задача – текст;
# o Оценка - цяло число в интервала [2…6]

bad_grade_number = int(input())

task_name = input()

average = 0
bad_grade_count = 0
count = 0
grade_sum = 0
enough_bad_grades = False
last_task = ''

while task_name != "Enough":
    grade = int(input())
    if grade > 4:
        count += 1
        grade_sum += grade
    else:
        bad_grade_count += 1
        if bad_grade_number == bad_grade_count:
            enough_bad_grades = True
            print(f"You need a break, {bad_grade_count} poor grades.")
            break
        count += 1
        grade_sum += grade
    last_task = task_name
    task_name = input()

if not enough_bad_grades:
    average = grade_sum / count
    print(f"Average score: {average :.2f}")
    print(f"Number of problems: {count}")
    print(f"Last problem: {last_task}")


# Изход
# · Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# o "Average score: {средна оценка}"
# o "Number of problems: {броя на всички задачи}"
# o "Last problem: {името на последната задача}"
# · Ако получи определеният брой незадоволителни оценки:
# o "You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.

