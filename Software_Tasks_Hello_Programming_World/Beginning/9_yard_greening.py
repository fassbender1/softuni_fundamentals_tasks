square_meters_for_maintenance = float(input())
price_for_1_square_meter = 7.61
price_without_discount = square_meters_for_maintenance * price_for_1_square_meter
price_with_discount = price_without_discount - (price_without_discount * 0.18)
the_discount = price_without_discount - price_with_discount

print(f"The final price is: {price_with_discount} lv.")
print(f"The discount is: {the_discount} lv.")
