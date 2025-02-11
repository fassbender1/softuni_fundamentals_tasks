gifts_planned = input().split()

# list_index = []
#
# for gift_index in range(len(gifts_planned)):
#     list_index.append(gift_index)

command = input()

while "No Money" not in command:
    parts = command.split()
    action = parts[0]

    if action == "OutOfStock":
        gift = parts[1]
        for each_gift in range(len(gifts_planned)):
            if gifts_planned[each_gift] == gift:
                gifts_planned[each_gift] = "None"
    elif action == "Required":
        index = int(parts[2])
        if 0 <= index < len(gifts_planned):
            gift = parts[1]
            gifts_planned[index] = gift
    elif action == "JustInCase":
        gift = parts[1]
        gifts_planned[-1] = gift

    command = input()


print(" ".join(each_gift for each_gift in gifts_planned if each_gift != "None"))
