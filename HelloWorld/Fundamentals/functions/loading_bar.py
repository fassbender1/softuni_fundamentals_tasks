def loading_bar(num):
    if num == 100:
        return "100% Complete!\n[%%%%%%%%%%]"

    percent_as_num = num // 10
    remaining_percent_as_num = 10 - percent_as_num
    return f"{num}% [{'%' * percent_as_num}{'.' * remaining_percent_as_num}]\nStill loading..."


number = int(input())
print(loading_bar(number))
