number_list = input().split()

rounded_values = []
for number in number_list:
    rounded_values.append(round(float(number)))

print(rounded_values)


