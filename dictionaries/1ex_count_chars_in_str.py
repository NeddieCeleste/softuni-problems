string = input()
letter_dict = {}
for letter in string:
    if letter != ' ':
        counted = string.count(letter)
        letter_dict[letter] = counted
for letter, counted in letter_dict.items():
    print(f"{letter} -> {counted}")
