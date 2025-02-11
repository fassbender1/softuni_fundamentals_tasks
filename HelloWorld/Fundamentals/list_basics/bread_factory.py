events = input().split("|")

current_energy = 100
startup_coins = 100

is_Bakery_open = True

for event in events:
    event_items = event.split("-")
    event_type = event_items[0]
    event_value = int(event_items[1])
    if event_type == "rest":
        startup_energy = current_energy
        current_energy += event_value
        if current_energy > 100:
            current_energy = 100
        energy_gained = current_energy - startup_energy
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {current_energy}.")
    elif event_type == "order":
        if current_energy >= 30:
            current_energy -= 30
            startup_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            current_energy += 50
            print("You had to rest!")
    else:
        if startup_coins >= event_value:
            startup_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            is_Bakery_open = False
            break

if is_Bakery_open:
    print("Day completed!")
    print(f"Coins: {startup_coins}")
    print(f"Energy: {current_energy}")
else:
    print(f"Closed! Cannot afford {event_type}.")

