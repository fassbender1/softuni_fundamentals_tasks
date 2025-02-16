def counter_strike(energy):

    command = input()
    battle_won_count = 0
    is_energy_enough = True

    while energy >= 0:
        if command == "End of battle":
            break
        distance = int(command)

        if energy < distance:
            is_energy_enough = False
            break
        elif energy > distance:
            energy -= distance
            battle_won_count += 1
            if battle_won_count % 3 == 0:
                energy += battle_won_count
        else:
            battle_won_count += 1
            if battle_won_count % 3 == 0:
                energy += battle_won_count
            energy -= distance

        command = input()

    if is_energy_enough:
        print(f"Won battles: {battle_won_count}. Energy left: {energy}")
    else:
        print(f"Not enough energy! Game ends with {battle_won_count} won battles and {energy} energy")


start_energy = int(input())
result = counter_strike(start_energy)
