# budget = int(input())
# command = input()
#
# while command != "End":
#     price = int(command)
#     budget -= price
#     if budget < 0:
#         print(f"You went in overdraft!")
#         break
#     elif budget == 0:
#         print(f"You bought everything needed.")
#         break
#     command = input()
#
# else:
#     print(f"You bought everything needed.")


budget = int(input())
total_price = 0

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break

    product_price = int(command)
    if total_price + product_price > budget:
        print("You went in overdraft!")
        break

    total_price += product_price
