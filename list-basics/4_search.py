n = int(input())
word = input()
strings = []

for _ in range(n):
    current_string = input()
    strings.append(current_string)

filtered_strings = []
for _string in strings:
    if word in _string:
        filtered_strings.append(_string)
print(strings)
print(filtered_strings)