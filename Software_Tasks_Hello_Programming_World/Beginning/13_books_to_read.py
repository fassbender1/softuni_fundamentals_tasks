total_pages_in_book = int(input())
pages_per_hour = int(input())
deadline_in_days = int(input())
hours_per_day = (total_pages_in_book // pages_per_hour) // deadline_in_days
print (hours_per_day)