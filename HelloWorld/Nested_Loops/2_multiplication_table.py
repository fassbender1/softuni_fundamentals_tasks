# Отпечатайте на конзолата таблицата за умножение за числата от 1 до 10 във формат:
# "{първи множител} * {втори множител} = {резултат}".

for number in range(1, 11):
    for number_2 in range(1, 11):
        result = number * number_2
        print(f"{number} * {number_2} = {result}")

