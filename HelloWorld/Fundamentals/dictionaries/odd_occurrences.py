elements = input().split()
element_dict = {}
for element in elements:
    element_lower = element.lower()
    if element_lower not in element_dict:
        element_dict[element_lower] = 0
    element_dict[element_lower] += 1

for key, value in element_dict.items():
    if value % 2 != 0:
        print(key, end=" ")

