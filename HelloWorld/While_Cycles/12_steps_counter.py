# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
# Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си.
# Напишете програма, която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня и когато
# постигне целта си да се изписва "Goal reached! Good job!"
# и колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките,
# които е извървяла докато се прибира. След което, ако не е успяла да постигне целта си,
# на конзолата трябва да се изпише: "{разликата между стъпките} more steps to reach goal."

steps = input()

steps_goal = 10000
steps_sum = 0
difference = 0
reached_goal = False

while steps != "Going home":
    current_steps = int(steps)
    steps_sum += current_steps
    if steps_sum >= steps_goal:
        break
    steps = input()

if steps == "Going home":
    extra_steps = int(input())
    steps_sum += extra_steps

if steps_sum < steps_goal:
    difference = steps_goal - steps_sum
    print(f"{difference} more steps to reach goal.")
else:
    difference = steps_sum - steps_goal
    print(f"Goal reached! Good job!")
    print(f"{difference} steps over the goal!")



