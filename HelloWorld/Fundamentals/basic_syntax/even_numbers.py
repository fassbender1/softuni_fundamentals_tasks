num = int(input())

is_odd = False

for i in range(1, num + 1):
    n = int(input())
    if n % 2 == 0:
        is_odd = False
    else:
        is_odd = True
        print(f"{n} is odd!")
        break

if not is_odd:
    print("All numbers are even.")
