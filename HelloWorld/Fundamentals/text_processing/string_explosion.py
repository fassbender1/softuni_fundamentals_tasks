def string_explosion(string):
    final_string = ""
    power = 0

    for index in range(len(string)):
        if power > 0 and string[index] != ">":
            power -= 1
        elif string[index] == ">":
            final_string += ">"
            power += int(string[index+1])
        else:
            final_string += string[index]

    return final_string


text = input()
result = string_explosion(text)
print(result)











