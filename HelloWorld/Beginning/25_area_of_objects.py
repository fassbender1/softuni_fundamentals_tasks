# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й. \
# Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
# На първия ред на входа се чете вида на фигурата (текст със следните възможности: square, rectangle, circle
# или triangle).
# ⦁	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# ⦁	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# ⦁	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# ⦁	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му
# и дължината на височината към нея
# Резултатът да се закръгли до 3 цифри след десетичната запетая.
object = str(input())

if object == "square":
    side = float(input())
    area = pow(side, 2)
    print(round(area, 3))

elif object == "rectangle":
    length = float(input())
    width = float(input())
    area = length * width
    print(round(area, 3))

elif object == "circle":
    from math import pi
    from math import pow
    radius = float(input())
    area = pi * (pow(radius, 2))
    print(round(area, 3))

elif object == "triangle":
    base = float(input())
    height = float(input())
    area = base * height / 2
    print(round(area, 3))

