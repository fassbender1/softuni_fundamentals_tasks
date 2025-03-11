force_side = {}
command = input()

while command != "Lumpawaroo":
    if " | " in command:
        side, user = command.split(" | ")
        user_is_part_of_the_force = False
        for list_with_force_users in force_side.values():
            if user in list_with_force_users:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if side not in force_side.keys():
                force_side[side] = []
            force_side[side].append(user)
    elif " -> " in command:
        user, side = command.split(" -> ")
        for list_with_force_users in force_side.values():
            if user in list_with_force_users:
                list_with_force_users.remove(user)
                break
        if side not in force_side.keys():
            force_side[side] = []
        force_side[side].append(user)
        print(f"{user} joins the {side} side!")

    command = input()

for sides, users in force_side.items():
    if users:
        print(f"Side: {sides}, Members: {len(users)}")
        for force_user in users:
            print(f"! {force_user}")















