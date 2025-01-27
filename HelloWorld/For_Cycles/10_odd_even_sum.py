# Да се напише програма, която чете n на брой цели числа, подадени от потребителя и проверява дали сумата от числата
# на четни позиции е равна на сумата на числата на нечетни позиции.
# · Ако сумите са равни да се отпечатат два реда: "Yes" и на нов ред "Sum = " + сумата;
# · Ако сумите не са равни да се отпечат два реда: "No" и на нов ред "Diff = " + разликата.
# Разликата се изчислява по абсолютна стойност.

number = int(input())

even_value, odd_value = 0, 0

for idx in range(number):
    new_input = int(input())
    if idx % 2 == 0:
        even_value += new_input
    else:
        odd_value += new_input

if even_value == odd_value:
    print("Yes")
    print(f"Sum = {even_value}")
else:
    difference = even_value - odd_value
    print("No")
    print(f"Diff = {abs(difference)}")


