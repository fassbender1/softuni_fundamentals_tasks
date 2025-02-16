def next_version(current_version):

    current_version = [int(digit) for digit in current_version.split(".")]
    current_version[-1] += 1

    for index in range(len(current_version) -1, -1, -1):
        if current_version[index] > 9:
            current_version[index] = 0
            current_version[index-1] += 1

    return ".".join([str(digit) for digit in current_version])


string = input()
result = next_version(string)
print(result)
