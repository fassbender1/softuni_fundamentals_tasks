# Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване. Според размера на групата,
# катерачите ще изкачват различни върхове.
# ⦁	Група до 5 човека – изкачват Мусала
# ⦁	Група от 6 до 12 човека – изкачват Монблан
# ⦁	Група от 13 до 25 човека – изкачват Килиманджаро
# ⦁	Група от 26 до 40 човека –  изкачват К2
# ⦁	Група от 41 или повече човека – изкачват Еверест
# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.

number_of_groups = int(input())

percent_1, percent_2, percent_3, percent_4, percent_5 = 0, 0, 0, 0, 0
count_1, count_2, count_3, count_4, count_5 = 0, 0, 0, 0, 0
total_climbers = 0

for _ in range(number_of_groups):
    climbers_in_group = int(input())
    total_climbers += climbers_in_group
    
    if climbers_in_group <= 5:
        count_1 += climbers_in_group
    elif 5 < climbers_in_group <= 12:
        count_2 += climbers_in_group
    elif 12 < climbers_in_group <= 25:
        count_3 += climbers_in_group
    elif 25 < climbers_in_group <= 40:
        count_4 += climbers_in_group
    elif climbers_in_group > 40:
        count_5 += climbers_in_group

percent_1 = count_1 / total_climbers * 100
percent_2 = count_2 / total_climbers * 100
percent_3 = count_3 / total_climbers * 100
percent_4 = count_4 / total_climbers * 100
percent_5 = count_5 / total_climbers * 100


print(f"{percent_1 :.2f}%")
print(f"{percent_2 :.2f}%")
print(f"{percent_3 :.2f}%")
print(f"{percent_4 :.2f}%")
print(f"{percent_5 :.2f}%")




# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# ⦁	На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# ⦁	За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]

# Изход
# Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00% с точност
# до втората цифра след десетичната запетая.
# ⦁	Първи ред - процентът изкачващи Мусала
# ⦁	Втори ред – процентът изкачващи Монблан
# ⦁	Трети ред – процентът изкачващи Килиманджаро
# ⦁	Четвърти ред – процентът изкачващи К2
# ⦁	Пети ред – процентът изкачващи Еверест
