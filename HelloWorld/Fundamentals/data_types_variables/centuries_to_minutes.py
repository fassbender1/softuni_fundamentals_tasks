centuries = int(input())

import math

centuries_to_years = centuries * 100
years_to_days = centuries_to_years * 365.2422
days_to_hours = math.floor(years_to_days) * 24
hours_to_minutes = math.floor(days_to_hours) * 60

print(f"{centuries} centuries = {centuries_to_years} years = {years_to_days :.0f} days = {days_to_hours} hours = {hours_to_minutes} minutes")

