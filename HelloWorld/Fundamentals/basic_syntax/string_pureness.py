num_of_strings = int(input())

for i in range(num_of_strings):
    string = input()
    if "," in string or \
            "." in string or \
            "_" in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")