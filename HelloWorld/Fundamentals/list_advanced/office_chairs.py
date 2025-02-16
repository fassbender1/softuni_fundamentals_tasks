def office_chairs(rooms):
    free_chairs = 0

    for room in range(1, rooms + 1):
        chairs, visitors = input().split()
        difference = len(chairs) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {room}")
        free_chairs += difference

    if free_chairs >= 0:
        print(f"Game On, {free_chairs} free chairs left")


num_rooms = int(input())
result = office_chairs(num_rooms)

