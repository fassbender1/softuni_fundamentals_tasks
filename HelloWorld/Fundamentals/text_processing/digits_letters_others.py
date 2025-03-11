text = input()

numbers = ""
letters = ""
symbols = ""

for element in text:
    if element.isnumeric():
        numbers += str(element)
    elif element.isalpha():
        letters += element
    else:
        symbols += element

print(numbers)
print(letters)
print(symbols)



