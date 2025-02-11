command = input()

total_coffees = 0

while command != "END":
    if command == "dog" or \
            command == "cat" or \
            command == "coding" or \
            command == "movie":
        num_coffees = 1
    elif command == "DOG" or \
            command == "CAT" or \
            command == "CODING" or \
            command == "MOVIE":
        num_coffees = 2
    else:
        command = input()
        continue

    total_coffees += num_coffees

    command = input()

if total_coffees > 5:
    print("You need extra sleep")
else:
    print(total_coffees)