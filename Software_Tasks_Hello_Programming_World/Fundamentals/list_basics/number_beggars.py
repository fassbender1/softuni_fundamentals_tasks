list_to_sum = input().split(", ")
beggars = int(input())

list_as_integers = []

for num in list_to_sum:
    list_as_integers.append(int(num))

beggars_sums = []
start_index = 0

for beggar in range(beggars):
    current_beggar_sum = 0
    for current_index in range(start_index, len(list_as_integers), beggars):
        current_beggar_sum += list_as_integers[current_index]
    beggars_sums.append(current_beggar_sum)
    start_index += 1

print(beggars_sums)
