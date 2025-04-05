import re

sentence = input()
word = input()

pattern = fr"\b{word}\b"
result = re.findall(pattern, sentence, re.IGNORECASE)
# pattern = fr"(?i)\b{word}\b"
# result = re.findall(pattern, sentence)

print(len(result))


