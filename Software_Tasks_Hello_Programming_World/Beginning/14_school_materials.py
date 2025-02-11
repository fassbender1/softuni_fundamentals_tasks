packs_of_pens = int(input()) * 5.80
packs_of_markers = int(input()) * 7.20
litres_of_detergent = int(input()) * 1.20
discount_percent = float(input()) / 100
amount_to_pay = packs_of_pens + packs_of_markers + litres_of_detergent
amount_with_discount = amount_to_pay - (amount_to_pay * discount_percent)
print(amount_with_discount)