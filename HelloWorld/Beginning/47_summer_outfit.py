# Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ. Напишете програма,
# която спрямо времето от денонощието и градусите да препоръча на Виктор какви дрехи да облече.
# Вашият приятел има различни планове за всеки етап от деня, които изискват и различен външен вид -
# може да ги видите от таблицата.
#
# От конзолата се четат точно два реда:
# · Градусите - цяло число;
# · Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".
#
# Като изход да се отпечата на конзолата на един ред: "It's {градуси} degrees, get your {облекло} and {обувки}."

degrees = int(input())
time_of_the_day = str(input())

Outfit = ""
Shoes = ""

if time_of_the_day == "Morning":

    if 10 <= degrees <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif 18 < degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif degrees >= 25:
        Outfit = "T-Shirt"
        Shoes = "Sandals"

elif time_of_the_day == "Afternoon":

    if 10 <= degrees <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif 18 < degrees <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif degrees >= 25:
        Outfit = "Swim Suit"
        Shoes = "Barefoot"

elif time_of_the_day == "Evening":

    if 10 <= degrees <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif 18 < degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif degrees >= 25:
        Outfit = "Shirt"
        Shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
