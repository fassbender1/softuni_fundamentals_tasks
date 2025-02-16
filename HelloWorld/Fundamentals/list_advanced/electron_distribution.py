def distribution(electrons):

    shells = []

    for shell in range(1, electrons + 1):
        max_electrons_in_shell = 2 * shell ** 2
        if electrons > max_electrons_in_shell:
            shells.append(max_electrons_in_shell)
            electrons -= max_electrons_in_shell
        else:
            shells.append(electrons)
            break
    return shells


number = int(input())
result = distribution(number)
print(result)