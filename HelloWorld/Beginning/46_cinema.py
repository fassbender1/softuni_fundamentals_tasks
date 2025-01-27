# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони.
# Има три вида прожекции с билети на различни цени:
# · Premiere - премиерна прожекция, на цена 12.00 лева;
# · Normal - стандартна прожекция, на цена 7.50 лева;
# · Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа),
# въведени от потребителя, и изчислява общите приходи от билети при пълна зала. Резултатът да се отпечата във
# формат 2 знака след десетичната точка.

screening_type = input()
number_of_rows = int(input())
number_of_columns = int(input())

projection_price = 0

capacity = number_of_columns * number_of_rows

if screening_type == "Discount":
    projection_price = 5.00
elif screening_type == "Normal":
    projection_price = 7.50
elif screening_type == "Premiere":
    projection_price = 12.00

total_income = capacity * projection_price

print(f'{total_income :.2f} leva')