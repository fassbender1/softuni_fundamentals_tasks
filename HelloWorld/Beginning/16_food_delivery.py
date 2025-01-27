chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.40
vegetarian_price = vegetarian_menu * 8.15
main_courses_price = chicken_price + fish_price + vegetarian_price
desert_price = main_courses_price * 0.2
total_price = main_courses_price + desert_price + 2.50
print(total_price)