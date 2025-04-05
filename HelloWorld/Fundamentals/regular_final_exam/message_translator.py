def check_if_valid():
    import re

    message_num = int(input())

    for _ in range(message_num):
        string = input()
        pattern = r"(!)[A-Z][a-z]{2,}(!):(\[)[A-Za-z]{8,}(\])"
        match = re.match(pattern, string)
        if match:
            entire_message = match[0]
            command, message = entire_message.split(":")
            translated = [str(ord(char)) for char in message[1:-1]]
            print(f"{command[1:-1]}: {' '.join(translated)}")
        else:
            print("The message is invalid")


check_if_valid()
