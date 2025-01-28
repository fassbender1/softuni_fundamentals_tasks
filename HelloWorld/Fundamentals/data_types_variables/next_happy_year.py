happy_year = int(input())

while True:
    happy_year += 1
    year_str = str(happy_year)

    if len(set(year_str)) == len(year_str):
        break

print(happy_year)