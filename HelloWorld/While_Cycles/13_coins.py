# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
# Напишете програма, която приема сума - рестото, което трябва да се върне и
# изчислява с колко най-малко монети може да стане това.

change = float(input())

count = 0

while change > 0:
    if change >= 2.00:
        change -= 2.00
    elif change >= 1.00:
        change -= 1.00
    elif change >= 0.50:
        change -= 0.50
    elif change >= 0.20:
        change -= 0.20
    elif change >= 0.10:
        change -= 0.10
    elif change >= 0.05:
        change -= 0.05
    elif change >= 0.02:
        change -= 0.02
    elif change >= 0.01:
        change -= 0.01
    count += 1
    change = round(change, 2)

print(count)


