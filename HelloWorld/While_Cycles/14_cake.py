# Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта. Той обаче не знае колко парчета могат
# да си вземат гостите от нея. Вашата задача е да напишете програма, която изчислява броя на парчетата,
# които гостите са взели преди тя да свърши. Ще получите размерите на тортата (широчина и дължина – цели числа и
# след това на всеки ред, до получаване на командата "STOP" или докато не свърши тортата, броят на парчетата,
# които гостите вземат от нея. Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# · "{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта;
# · "No more cake left! You need {брой недостигащи парчета} pieces more."

width = int(input())
length = int(input())

cake_left = True

cake_size = width * length

pieces_taken = input()

while pieces_taken != "STOP":
    additional_pieces = int(pieces_taken)
    if additional_pieces >= cake_size:
        additional_pieces -= cake_size
        cake_left = False
        print(f"No more cake left! You need {abs(additional_pieces)} pieces more.")
        break
    cake_size -= additional_pieces
    pieces_taken = input()

if cake_left:
    print(f"{cake_size} pieces are left.")
