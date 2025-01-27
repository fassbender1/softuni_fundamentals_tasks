# Млад програмист разполага с определен бюджет и свободно време в даден сезон. Напишете програма, която да приема на
# входа бюджета и сезона, а на изхода да изкарва къде ще почива програмистът и колко ще похарчи.
# Бюджетът определя дестинацията, а сезонът - колко от бюджета ще изхарчи. Ако е лято ще почива на къмпинг, а зимата в
# хотел. Ако е в Европа, независимо от сезона, ще почива в хотел. Всеки къмпинг или хотел, според дестинацията,
# има собствена цена, която отговаря на даден процент от бюджета:
# · При 100 лв. или по-малко - някъде в България:
# o Лято - 30% от бюджета;
# o Зима - 70% от бюджета.
# · При 1000 лв. или по малко - някъде на Балканите:
# o Лято - 40% от бюджета;
# o Зима - 80% от бюджета.
# · При повече от 1000 лв. - някъде из Европа:
# o При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.

budget = float(input())
season = input()

destination = ""
vacation_type = ""
vacation_cost = 0


if budget <= 100:
    destination = "Bulgaria"
    if season == "winter":
        vacation_type = "Hotel"
        vacation_cost = budget * 0.70
    elif season == "summer":
        vacation_type = "Camp"
        vacation_cost = budget * 0.30

elif budget <= 1000:
    destination = "Balkans"
    if season == "winter":
        vacation_type = "Hotel"
        vacation_cost = budget * 0.80
    elif season == "summer":
        vacation_type = "Camp"
        vacation_cost = budget * 0.40

elif budget > 1000:
    destination = "Europe"
    vacation_type = "Hotel"
    vacation_cost = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{vacation_type} - {vacation_cost :.2f}")



# Изход
# На конзолата трябва да се отпечатат два реда:
# · "Somewhere in [дестинация]" измежду "Bulgaria", "Balkans" и "Europe"
# · "{Вид почивка} - {Похарчена сума}":
# o Почивката може да е между "Camp" и "Hotel"
# o Сумата трябва да бъде форматирана с точност до вторият знак след десетичната запетая

