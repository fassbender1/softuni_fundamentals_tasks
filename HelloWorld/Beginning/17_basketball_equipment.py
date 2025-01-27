year_training_price = int(input())

sneakers = year_training_price - (year_training_price * 0.4)
jersey = sneakers - (sneakers * 0.2)
ball = jersey / 4
accessories = ball / 5
total_training_price = year_training_price + sneakers + jersey + ball + accessories

print(total_training_price)