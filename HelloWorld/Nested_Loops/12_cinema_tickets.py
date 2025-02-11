# Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от продадените билети:
# студентски(student), стандартен(standard) и детски(kid), за всички прожекции.
# Трябва да изчислите и колко процента от залата е запълнена за всяка една прожекция.
# Вход
# Входът е поредица от цели числа и текст:
# · На първия ред до получаване на командата "Finish" - име на филма – текст
# · На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# · За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
# o Типа на закупения билет - текст ("student", "standard", "kid")
# Изход
# На конзолата трябва да се печатат следните редове:
# · След всеки филм да се отпечата, колко процента от кино залата е пълна
# "{името на филма} - {процент запълненост на залата}% full."
# · При получаване на командата "Finish" да се отпечатат четири реда:
# o "Total tickets: {общият брой закупени билети за всички филми}"
# o "{процент на студентските билети}% student tickets."
# o "{процент на стандартните билети}% standard tickets."
# o "{процент на детските билети}% kids tickets."

command = input()

total_student = 0
total_standard = 0
total_kid = 0
total_tickets = 0

is_finished = False

while command != "Finish":
    movie_name = command
    available_seats = int(input())
    ticket_type = input()

    student_tickets = 0
    standard_tickets = 0
    kid_tickets = 0
    percent_seats_taken = 0
    tickets_per_movie = 0

    while ticket_type != "End":
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        tickets_per_movie = student_tickets + standard_tickets + kid_tickets
        percent_seats_taken = (tickets_per_movie / available_seats) * 100

        if tickets_per_movie >= available_seats:
            break

        ticket_type = input()

    print(f"{movie_name} - {percent_seats_taken :.2f}% full.")

    total_student += student_tickets
    total_standard += standard_tickets
    total_kid += kid_tickets
    total_tickets += tickets_per_movie

    movie_name = input()

    if movie_name == "Finish":
        is_finished = True
        break

percent_standard = (total_standard / total_tickets) * 100
percent_student = (total_student / total_tickets) * 100
percent_kid = (total_kid / total_tickets) * 100

if is_finished:
    print(f"Total tickets: {total_tickets}")
    print(f"{percent_student :.2f}% student tickets.")
    print(f"{percent_standard :.2f}% standard tickets.")
    print(f"{percent_kid :.2f}% kids tickets.")