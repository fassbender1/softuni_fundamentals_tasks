def the_office(employees, factor):
    employees = list(map(lambda x: int(x) * factor, employees))
    filtered = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))
    if len(filtered) >= len(employees) / 2:
        return f"Score: {len(filtered)}/{len(employees)}. Employees are happy!"
    else:
        return f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!"


employees_happiness = input().split()
happiness_factor = int(input())
result = the_office(employees_happiness, happiness_factor)
print(result)
