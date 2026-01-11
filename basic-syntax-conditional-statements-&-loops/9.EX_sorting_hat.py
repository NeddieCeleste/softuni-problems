names = input()
char_count = len(names)

while names not in ('Welcome!', 'Voldemort'):
    if char_count < 5:
        print(f"{names} goes to Gryffindor.")
    elif char_count == 5:
        print(f"{names} goes to Slytherin.")
    elif char_count == 6:
        print(f"{names} goes to Ravenclaw.")
    elif char_count > 6:
        print(f"{names} goes to Hufflepuff.")
    names = input()
    char_count = len(names)
if names == 'Voldemort':
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")
