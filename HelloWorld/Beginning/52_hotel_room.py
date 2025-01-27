# Хотел предлага 2 вида стаи: студио и апартамент. Напишете програма, която изчислява цената за целия
# престой за студио и апартамент. Цените зависят от месеца на престоя:
# Предлагат се и следните отстъпки:
# · За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# · За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# · За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# · За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

# · На първия ред е месецът - May, June, July, August, September или October;

month = input()
number_of_nights = int(input())

price_per_night_studio = 0
price_per_night_apartment = 0
total_price_studio = 0
total_price_apartment = 0

if month == "May" or month == "October":
    price_per_night_studio = 50
    price_per_night_apartment = 65

    if 7 < number_of_nights <= 14:
        price_per_night_studio *= 0.95
    elif number_of_nights > 14:
        price_per_night_studio *= 0.70
        price_per_night_apartment *= 0.90

elif month == "June" or month == "September":
    price_per_night_studio = 75.20
    price_per_night_apartment = 68.70

    if number_of_nights > 14:
        price_per_night_studio *= 0.80
        price_per_night_apartment *= 0.90

elif month == "July" or month == "August":
    price_per_night_studio = 76
    price_per_night_apartment = 77

    if number_of_nights > 14:
        price_per_night_apartment *= 0.90

total_price_studio = price_per_night_studio * number_of_nights
total_price_apartment = price_per_night_apartment * number_of_nights

print(f"Apartment: {total_price_apartment :.2f} lv.")
print(f"Studio: {total_price_studio :.2f} lv.")









# Изход
# Да се отпечатат на конзолата 2 реда:
# · На първия ред: "Apartment: {цена за целият престой} lv."
# · На втория ред: "Studio: {цена за целият престой} lv."
# Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.