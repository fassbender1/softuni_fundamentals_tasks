# Дадено число е валидно, ако е в диапазона [100…200] или е 0. Да се напише програма,
# която чете цяло число, въведено от потребителя, и печата "invalid" ако въведеното число не е валидно.

# number = int(input())
#
# if 100 <= number <= 200 or number == 0:
#     print()
# else:
#     print("invalid")
#

number = int(input())

valid = 100 <= number <= 200 or number == 0

if not valid:
    print("invalid")