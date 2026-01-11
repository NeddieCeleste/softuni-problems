quantity = int(input())
result = 0
for i in range(quantity):
    character = input()
    result += ord(character)

print(f"The sum equals: {result}")