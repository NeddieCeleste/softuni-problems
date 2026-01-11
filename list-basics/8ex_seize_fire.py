fire_cell_list = ["High", "Medium", "Low"]
cells = input().split("#")
water_total = int(input())
type_cell = []
value_cell = []
effort = 0.00
total_fire = 0
print("Cells:")
for cell in cells:
    separated_cell = cell.split(" = ")
    type_list = separated_cell[0:1]
    value_list = separated_cell[1:]
    for i in type_list:
        type_cell.append(str(i))
        for index in value_list:
            value_cell.append(int(index))
            if i == "High":
                if 81 <= int(index) <= 125:
                    if water_total >= int(index):
                        water_total -= int(index)
                        effort += int(index) * 0.25
                        total_fire += int(index)
                        print(f"- {index}")
                else:
                    continue
            elif i == "Medium":
                if 51 <= int(index) <= 80:
                    if water_total >= int(index):
                        water_total -= int(index)
                        effort += int(index) * 0.25
                        total_fire += int(index)
                        print(f"- {index}")
                else:
                    continue
            elif i == "Low":
                if 1 <= int(index) <= 50:
                    if water_total >= int(index):
                        water_total -= int(index)
                        effort += int(index) * 0.25
                        total_fire += int(index)
                        print(f"- {index}")
                else:
                    continue
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
