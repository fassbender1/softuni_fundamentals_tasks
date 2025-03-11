countries = input().split(", ")
capitals = input().split(", ")

alignment = {key: value for key, value in zip(countries, capitals)}

for country, capital in alignment.items():
    print(f"{country} -> {capital}")

