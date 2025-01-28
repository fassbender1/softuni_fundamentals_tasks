group_size = int(input())
days = int(input())

amount_received = 0
coins_collected = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5
    if i % 3 == 0:
        coins_collected -= (group_size * 3)
    if i % 5 == 0:
        coins_collected += (group_size * 20)
        if i % 3 == 0:
            coins_collected -= (group_size * 2)
    coins_collected += 50
    coins_collected -= (group_size * 2)

coins_per_person = coins_collected / group_size

print(f"{group_size} companions received {int(coins_per_person)} coins each.")