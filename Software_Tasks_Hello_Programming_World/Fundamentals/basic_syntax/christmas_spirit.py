decorations_quantity = int(input())
days_until = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

ornament_points = 5
skirt_points = 3
garland_points = 10
light_points = 17

total_cost = 0
total_spirit = 0

for current_day in range(1, days_until + 1):
    if current_day % 11 == 0:
        decorations_quantity += 2
    if current_day % 2 == 0:
        total_cost += ornament_set_price * decorations_quantity
        total_spirit += ornament_points
    if current_day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * decorations_quantity
        total_spirit += (skirt_points + garland_points)
    if current_day % 5 == 0:
        total_cost += tree_lights_price * decorations_quantity
        total_spirit += light_points
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += (tree_skirt_price + tree_garland_price + tree_lights_price)

if days_until % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")


