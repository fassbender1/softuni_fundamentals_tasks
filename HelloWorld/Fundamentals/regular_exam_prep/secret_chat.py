def message_func():
    concealed_message = input()
    command = input()
    commands = []

    while "Reveal" not in command:
        commands.append(command)
        command = input()

    for current_command in commands:
        parts = current_command.split(":|:")
        action = parts[0]

        if action == "InsertSpace":
            index = int(parts[1])
            concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        elif action == "Reverse":
            substring = parts[1]
            if substring in concealed_message:
                concealed_message = concealed_message.replace(substring, '', 1) + substring[::-1]
            else:
                print("error")
                continue
        elif action == "ChangeAll":
            substring, replacement = parts[1], parts[2]
            concealed_message = concealed_message.replace(substring, replacement)

        print(concealed_message)

    print(f"You have a new text message: {concealed_message}")


message_func()

