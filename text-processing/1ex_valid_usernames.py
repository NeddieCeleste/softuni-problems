usernames = input().split(', ')
for username in usernames:
    username_is_valid = True
    if not (3 <= len(username) <= 16):
        username_is_valid = False
    for symbol in username:
        if not (symbol.isalnum() or symbol == '_' or symbol == '-'):
            username_is_valid = False
            break
    if " " in username:
        username_is_valid = False
    if username_is_valid:
        print(username)