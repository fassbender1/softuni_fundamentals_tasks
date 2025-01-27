# Напишете програма, която чете цяло число от конзолата и на всеки следващ ред цели числа, докато тяхната сума стане
# по-голяма или равна на първоначалното число. След приключване на четенето да се отпечата сумата на въведените числа

number = int(input())
sumo = 0

while True:
    next_number = int(input())
    sumo += next_number
    if sumo >= number:
        print(sumo)
        break


# number = int(input())
# sumo = 0
#
# while sumo < number:
#     next_number = int(input())
#     sumo += next_number
#
# print(sumo)
