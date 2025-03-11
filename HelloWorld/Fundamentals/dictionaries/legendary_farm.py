currency = {"shards":  0, "fragments": 0, "motes": 0}
legendary_obtained = False
legendary_item = ""

while not legendary_obtained:
    currency_input = input().split()
    for index in range(0, len(currency_input), 2):
        key = currency_input[index + 1].lower()
        value = int(currency_input[index])
        if key not in currency.keys():
            currency[key] = 0
        currency[key] += value
        if currency["shards"] > 249:
            legendary_item = "Shadowmourne"
            currency["shards"] -= 250
            legendary_obtained = True
        elif currency["fragments"] > 249:
            currency["fragments"] -= 250
            legendary_item = "Valanyr"
            legendary_obtained = True
        elif currency["motes"] > 249:
            currency["motes"] -= 250
            legendary_item = "Dragonwrath"
            legendary_obtained = True
        if legendary_obtained:
            break

print(f"{legendary_item} obtained!")
for key, value in currency.items():
    print(f"{key}: {value}")

