def order_products(product_type, quantity):
    if product_type == 'coffee':
        price = 1.50
    elif product_type == 'coke':
        price = 1.40
    elif product_type == 'water':
        price = 1.00
    elif product_type == 'snacks':
        price = 2.00
    total_price = quantity * price
    return total_price

product_type_ = input()
quantity_ = int(input())
final_price = order_products(product_type_, quantity_)
print(f'{final_price:.2f}')
