# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop".
# Да се намери сумата на всички въведени прости и сумата на всички въведени непрости числа.
# Тъй като по дефиниция от математиката отрицателните числа не могат да бъдат прости,
# ако на входа се подаде отрицателно число, да се изведе следното съобщение "Number is negative.".
# В този случай въведено число се игнорира и не се прибавя към нито една от двете суми,
# а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.
#
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# · "Sum of all prime numbers is: {prime numbers sum}"
# · "Sum of all non prime numbers is: {non-prime numbers sum}"

command = input()

sum_primes = 0
sum_non_primes = 0

while command != "stop":

    number_input = int(command)

    if number_input < 0:
        print(f"Number is negative")
        command = input()
        continue

    is_prime = True
    
    for divisor in range(2, number_input):
        if number_input % divisor == 0:
            is_prime = False
            break

    if not is_prime:
        sum_non_primes += number_input
    else:
        sum_primes += number_input

    command = input()

print(f"Sum of all prime numbers is: {sum_primes}")
print(f"Sum of all non prime numbers is: {sum_non_primes}")
