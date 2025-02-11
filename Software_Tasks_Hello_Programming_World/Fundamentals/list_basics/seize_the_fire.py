fire_type_cell = input().split("#")
total_water = int(input())

effort = 0
total_fire = 0
cells = []

for each_fire_cell in fire_type_cell:
    fire_and_cell = each_fire_cell.split(" = ")
    fire = fire_and_cell[0]
    cell = int(fire_and_cell[1])

    if fire == "High" and 81 <= cell <= 125 and total_water >= cell:
        cells.append(cell)
        effort += cell * 0.25
        total_water -= cell
        total_fire += cell
    elif fire == "Medium" and 51 <= cell <= 80 and total_water >= cell:
        cells.append(cell)
        effort += cell * 0.25
        total_water -= cell
        total_fire += cell
    elif fire == "Low" and 1 <= cell <= 50 and total_water >= cell:
        cells.append(cell)
        effort += cell * 0.25
        total_water -= cell
        total_fire += cell

print(f"Cells:")

for cell in cells:
    print(f" - {cell}")

print(f"Effort: {effort :.2f}")
print(f"Total Fire: {total_fire}")
