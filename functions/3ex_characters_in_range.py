def all_the_symbols(first: str, second: str) -> str:
    collected_symbols = []
    for current_symbol in range(ord(first) + 1, ord(second)):
        collected_symbols.append(chr(current_symbol))
    return collected_symbols


first_character = input()
second_character = input()
symbols = all_the_symbols(first_character, second_character)
print(" ".join(symbols))