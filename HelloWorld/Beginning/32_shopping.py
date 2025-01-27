# Петър иска да купи N видеокарти, M процесора и P на брой рам памет. Ако броя на видеокартите е по-голям от този на
# процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
# ⦁	Видеокарта – 250 лв./бр.
# ⦁	Процесор – 35% от цената на закупените видеокарти/бр.
# ⦁	Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.

# Вход
# Входът се състои от четири реда:
# ⦁	Бюджетът на Петър - реално число в интервала [1.0…100000.0]
Petar_budget = float(input())
# ⦁	Броят видеокарти - цяло число в интервала [1…100]
VGA_number = int(input())
# ⦁	Броят процесори - цяло число в интервала [1…100]
CPU_number = int(input())
# ⦁	Броят рам памет - цяло число в интервала [1…100]
RAM_number = int(input())

VGA_price = VGA_number * 250
CPU_price = VGA_price * 0.35 * CPU_number
RAM_price = VGA_price * 0.10 * RAM_number

total_cost = VGA_price + CPU_price + RAM_price

if VGA_number > CPU_number:
    total_cost *= 0.85

if total_cost <= Petar_budget:
    money_left = Petar_budget - total_cost
    print(f'You have {money_left:.2f} leva left!')
else:
    money_needed = total_cost - Petar_budget
    print (f'Not enough money! You need {money_needed:.2f} leva more!')

# Изход
# На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:
# ⦁	Ако бюджета е достатъчен:
# "You have {остатъчен бюджет} leva left!"
# ⦁	Ако сумата надхвърля бюджета:
# "Not enough money! You need {нужна сума} leva more!"
# Резултатът да се форматира до втория знак след десетичната запетая.
