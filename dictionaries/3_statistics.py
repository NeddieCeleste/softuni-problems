stock = {}

while True:
    line = input()

    if line == 'statistics':
        break

    product, quantity = line.split(': ')

    if product in stock:
        stock[product] += int(quantity)
    else:
        stock[product] = int(quantity)

product_count = len(stock)
total_count = sum(stock.values())
print("Products in stock:")

for product, quantity in stock.items():
    print(f"- {product}: {quantity}")

print(f'Total Products: {product_count}')
print(f'Total Quantity: {total_count}')