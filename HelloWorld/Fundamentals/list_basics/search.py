number = int(input())
search_word = input()

entire_input = []
search_match = []

for i in range(number):
    list_input = input()
    if search_word in list_input:
        search_match.append(list_input)
        entire_input.append(list_input)
    else:
        entire_input.append(list_input)

print(entire_input)
print(search_match)