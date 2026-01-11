text = input()

result = ""
current_string = ""
current_number = ""

for ch in text:
    if ch.isdigit():
        current_number += ch
    else:
        if current_number != "":
            result += current_string.upper() * int(current_number)
            current_string = ""
            current_number = ""

        current_string += ch
if current_string and current_number:
    result += current_string.upper() * int(current_number)

unique_symbols = len(set(result))

print(f"Unique symbols used: {unique_symbols}")
print(result)