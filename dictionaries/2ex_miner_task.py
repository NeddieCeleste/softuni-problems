resources = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource in resources:
        resources[resource] = resources[resource] + quantity
    else:
        resources[resource] = quantity
for resource, quantities in resources.items():
    print(f"{resource} -> {quantities}")
