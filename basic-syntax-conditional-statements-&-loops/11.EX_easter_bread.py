from math import floor

budget = float(input())
flour_kilo_price = float(input())
eggs_price = flour_kilo_price * 0.75
milk_liter_price = flour_kilo_price * 1.25
loaf = flour_kilo_price + eggs_price + (milk_liter_price / 4)
total = floor(budget / loaf)
colored_eggs = 0
for count in range(1, total + 1):
    colored_eggs += 3
    if count % 3 == 0:
        colored_eggs -= (count - 2)

leftover = budget - (total * loaf)

print(f"You made {total} loaves of Easter bread! Now you have {colored_eggs} eggs and {leftover:.2f}BGN left.")