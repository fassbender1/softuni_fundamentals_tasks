def string_manipulation():
    text = input()

    while True:
        command = input()
        if command == "End":
            break

        parts = command.split(" ")

        action = parts[0]

        if action == "Translate":
            char = parts[1]
            replacement = parts[2]
            text = text.replace(char, replacement)
            print(text)

        elif action == "Includes":
            substring = " ".join(parts[1:])
            print(str(substring in text))

        elif action == "Start":
            substring = " ".join(parts[1:])
            print(str(text.startswith(substring)))

        elif action == "Lowercase":
            text = text.lower()
            print(text)

        elif action == "FindIndex":
            char = parts[1]
            print(text.rfind(char))

        elif action == "Remove":
            startIndex = int(parts[1])
            count = int(parts[2])
            text = text[:startIndex] + text[startIndex + count:]
            print(text)


string_manipulation()


