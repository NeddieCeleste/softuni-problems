command = input()
coffee_count = 0
while command != 'END':
    if command in ('coding', 'CODING', 'dog', 'DOG', 'cat', 'CAT', 'movie', 'MOVIE'):
        if command.isupper():
            coffee_count += 2
        else:
            coffee_count += 1
    command = input()
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)

