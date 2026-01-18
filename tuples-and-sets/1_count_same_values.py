values = tuple(float(x) for x in input().split())
data = {}

for element in values:
    if element not in data:
        data[element] = values.count(element)

for key, value in data.items():
    print(f"{key:.1f} - {value} times")