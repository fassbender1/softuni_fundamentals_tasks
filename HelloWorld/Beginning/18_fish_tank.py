length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

area_in_meters = length * width * height
area_in_litres = area_in_meters * 0.001
required_litres = area_in_litres * (1 - percentage / 100)

print(required_litres)