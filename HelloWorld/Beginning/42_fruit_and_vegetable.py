# Да се напише програма, която чете име на продукт, въведено от потребителя, и проверява дали е плод или зеленчук.
# · Плодовете "fruit" имат следните възможни стойности: banana, apple, kiwi, cherry, lemon и grapes;
# · Зеленчуците "vegetable" имат следните възможни стойности: tomato, cucumber, pepper и carrot;
# · Всички останали са "unknown".
# Да се изведе "fruit", "vegetable" или "unknown" според въведения продукт

sort_to_check = input()
result = ""

if (sort_to_check == "banana"
        or sort_to_check == "apple"
        or sort_to_check == "kiwi"
        or sort_to_check == "kiwi"
        or sort_to_check == "cherry"
        or sort_to_check == "lemon"
        or sort_to_check == "grapes"):
    result = "fruit"

elif (sort_to_check == "tomato"
      or sort_to_check == "cucumber"
      or sort_to_check == "pepper"
      or sort_to_check == "carrot"):
    result = "vegetable"
else:
    result = "unknown"

print(result)
