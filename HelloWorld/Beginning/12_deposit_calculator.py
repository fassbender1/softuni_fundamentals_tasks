deposit_amount = float(input())
deposit_period = int(input())
yearly_interest_percentage = float(input())
interest = deposit_amount * (yearly_interest_percentage / 100)
interest_per_month = interest / 12
end_sum = deposit_amount + deposit_period * interest_per_month
print(end_sum)