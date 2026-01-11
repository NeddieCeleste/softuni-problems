food_list = {}
foods = input().split()
for food in range(0, len(foods), 2):
    available_food = foods[food]
    quantities = int(foods[food + 1])
    food_list[available_food] = quantities
print(food_list)
