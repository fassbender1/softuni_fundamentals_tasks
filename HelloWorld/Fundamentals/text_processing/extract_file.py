def extract_file(string):
    list = string.split("\\")
    filename = list[-1]
    name, extension = filename.split(".")
    return f"File name: {name}\n" \
           f"File extension: {extension}"


text = input()
result = extract_file(text)
print(result)

