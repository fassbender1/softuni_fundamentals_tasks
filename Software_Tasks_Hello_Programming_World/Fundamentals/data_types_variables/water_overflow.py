num_of_entries = int(input())

capacity = 255
capacity_incremented = 0

for i in range(num_of_entries):
    liters_input = int(input())
    capacity -= liters_input
    if capacity < 0:
        capacity += liters_input
        print(f"Insufficient capacity!")
    else:
        capacity_incremented += liters_input

print(capacity_incremented)


