parking = {}
number_of_commands = int(input())

for command in range(number_of_commands):
    current_command = input().split()
    action = current_command[0]
    if action == "register":
        name, car_number = current_command[1], current_command[2]
        if name in parking.keys():
            print(f"ERROR: already registered with plate number {car_number}")
        else:
            parking[name] = car_number
            print(f"{name} registered {car_number} successfully")
    elif action == "unregister":
        name = current_command[1]
        if name not in parking.keys():
            print(f"ERROR: user {name} not found")
        else:
            del parking[name]
            print(f"{name} unregistered successfully")

for user, plate in parking.items():
    print(f"{user} => {plate}")
