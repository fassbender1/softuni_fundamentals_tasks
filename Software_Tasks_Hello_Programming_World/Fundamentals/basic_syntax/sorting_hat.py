name = input()

is_sorted = True

while name != "Welcome!":
    chars = len(name)
    if name == "Voldemort":
        print("You must not speak of that name!")
        is_sorted = False
        break
    elif chars < 5:
        print(f"{name} goes to Gryffindor.")
    elif chars == 5:
        print(f"{name} goes to Slytherin.")
    elif chars == 6:
        print(f"{name} goes to Ravenclaw.")
    elif chars > 6:
        print(f"{name} goes to Hufflepuff.")

    name = input()

if is_sorted:
    print(f"Welcome to Hogwarts.")