data = input()
phonebook = {}

while True:
    if "-" not in data:
        break
    name, number = data.split("-")
    phonebook[name] = number

    data = input()

entries = int(data)

for _ in range(entries):
    name = input()
    if name not in phonebook:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook[name]}")

