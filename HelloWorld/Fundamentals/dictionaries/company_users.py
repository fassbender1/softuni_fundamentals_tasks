command = input()
employees_per_company = {}

while command != "End":
    company, employee = command.split(" -> ")
    if company not in employees_per_company.keys():
        employees_per_company[company] = []

    if employee not in employees_per_company[company]:
        employees_per_company[company].append(employee)

    command = input()


for company_name, employee_id in employees_per_company.items():
    print(f"{company_name}")
    for employee_value in employee_id:
        print(f"-- {employee_value}")

