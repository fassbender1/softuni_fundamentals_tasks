# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да събере
# необходимата сума. Тя спестява или харчи част от парите си всеки ден.
# Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# Вход
# От конзолата се четат:
# · Пари, нужни за екскурзията - реално число;
# · Налични пари - реално число.
# След това многократно се четат по два реда:
# · Вид действие – текст с две възможности: "spend" или "save";
# · Сумата, която ще спести/похарчи - реално число.

needed_money = float(input())
available_money = float(input())

days_count = 0
days_spending = 0

spent_5_days = False

while needed_money > available_money:
    action = input()
    if action == "spend":
        amount = float(input())
        days_count += 1
        days_spending += 1
        if days_spending == 5:
            spent_5_days = True
            print(f"You can't save the money.")
            print(f"{days_count}")
            break
        elif amount > available_money:
            available_money = 0
            continue
        available_money -= amount
    elif action == "save":
        amount = float(input())
        days_count += 1
        days_spending = 0
        available_money += amount

if not spent_5_days:
    print(f"You saved the money for {days_count} days.")



# Изход
# Програмата трябва да приключи при следните случаи:
# · Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# o "You can't save the money."
# o "{Общ брой изминали дни}"
# · Ако Джеси събере парите за почивката, на конзолата се изписва:
# o "You saved the money for {общ брой изминали дни} days."