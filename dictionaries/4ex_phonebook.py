phonebook = {}

while True:
    entry = input()
    if "-" not in entry:
        break
    name, number = entry.split("-")
    phonebook[name] = number
searches = int(entry)
for search in range(searches):
    searched_name = input()
    if searched_name in phonebook.keys():
        number = phonebook[searched_name]
        print(f"{searched_name} -> {number}")
    else:
        print(f"Contact {searched_name} does not exist.")