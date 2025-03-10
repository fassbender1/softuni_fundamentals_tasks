# Григор Димитров е тенисист, чиято следваща цел е изкачването в световната ранглиста по тенис за мъже.
# През годината Гришо участва в определен брой турнири, като за всеки турнир получава точки, които зависят от
# позицията, на която е завършил в турнира. Има три варианта за завършване на турнир:
# ⦁	W - ако е победител получава 2000 точки
# ⦁	F - ако е финалист получава 1200 точки
# ⦁	SF - ако е полуфиналист получава 720 точки
# Напишете програма, която изчислява колко ще са точките на Григор след изиграване на всички турнири,
# като знаете с колко точки стартира сезона. Също изчислете колко точки средно печели от всички изиграни турнири и
# колко процента от турнирите е спечелил.

import math

number_of_tournaments = int(input())
starting_points = int(input())

total_points = 0
tournaments_won = 0

for _ in range(number_of_tournaments):
    current_result = input()
    if current_result == "W":
        tournaments_won += 1
        total_points += 2000
    elif current_result == "F":
        total_points += 1200
    elif current_result == "SF":
        total_points += 720

average = total_points / number_of_tournaments
total_points += starting_points
percent_won = tournaments_won / number_of_tournaments * 100

# Вход
# От конзолата първо се четат два реда:
# ⦁	Брой турнири, в които е участвал – цяло число в интервала [1…20]
# ⦁	Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# ⦁	Достигнат етап от турнира – текст – "W", "F" или "SF"

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average)}")
print(f"{percent_won :.2f}%")

# Изход
# Отпечатват се три реда в следния формат:
# ⦁	"Final points: {брой точки след изиграните турнири}"
# ⦁	"Average points: {средно колко точки печели за турнир}"
# ⦁	"{процент спечелени турнири}%"
# Средните точки да бъдат закръглени към най-близкото цяло число надолу, а процентът да се форматира до
# втората цифра след десетичния знак.
