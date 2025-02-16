def the_lift(people_waiting, lift_space):
    max_capacity = 4

    for lift in range(len(lift_space)):
        available_space = max_capacity - lift_space[lift]
        if people_waiting >= available_space:
            lift_space[lift] += available_space
            people_waiting -= available_space
        else:
            lift_space[lift] += people_waiting
            people_waiting = 0
            break

    if people_waiting == 0 and any(wagon < max_capacity for wagon in lift_space):
        print(f"The lift has empty spots!")
    elif people_waiting > 0 and all(wagon == max_capacity for wagon in lift_space):
        print(f"There isn't enough space! {people_waiting} people in a queue!")

    print(" ".join([str(wagon) for wagon in lift_space]))


people = int(input())
initial_lift_space = list(map(int, input().split()))
result = the_lift(people, initial_lift_space)
