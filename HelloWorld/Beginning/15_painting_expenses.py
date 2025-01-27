nylon_square_meters = int(input())
paint_litres = int(input())
paint_thinner = int(input())
hours = int(input())

nylons_total = (nylon_square_meters + 2) * 1.50
paint_total = (paint_litres + (paint_litres * 0.1)) * 14.50
thinner = paint_thinner * 5
material_expenses = nylons_total + paint_total + thinner + 0.40
worker_expenses = (material_expenses * 0.3) * hours
total_expenses = material_expenses + worker_expenses

print(total_expenses)
