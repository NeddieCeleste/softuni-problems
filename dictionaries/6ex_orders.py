products = {}

while True:
    line = input()
    if line == "buy":
        break

    name, price, quantity = line.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = [price, quantity]
    else:
        products[name][0] = price
        products[name][1] += quantity

for name, (price, qty) in products.items():
    print(f"{name} -> {price * qty:.2f}")