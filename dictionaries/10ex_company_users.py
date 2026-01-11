company_dictionary = {}

while True:
    command = input()
    if command == "End":
        break
    company_name, employee_id = command.split(" -> ")
    if company_name not in company_dictionary:
        company_dictionary[company_name] = [employee_id]
    else:
        if employee_id not in company_dictionary[company_name]:
            company_dictionary[company_name].append(employee_id)

for company_name in company_dictionary.keys():
    print(company_name)
    for employee_id in company_dictionary[company_name]:
        print(f"-- {employee_id}")