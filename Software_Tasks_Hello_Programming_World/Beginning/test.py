
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

for first in range(1, num_1 + 1):
    if first % 2 != 0:
        continue
    for second in range(2, num_2 + 1):
        is_prime = True
        for divisor in range(2, second):
            if second % divisor == 0:
                is_prime = False
                break
        if is_prime:
            for third in range(1, num_3 + 1):
                if third % 2 != 0:
                    continue
                print(f"{first} {second} {third}")

