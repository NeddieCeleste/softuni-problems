strings = input().split()
new_text = [text * len(text) for text in strings]
print(''.join(new_text))