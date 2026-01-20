from collections import deque

expression = input().split()
numbers = deque()

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

for ch in expression:
    if ch not in "+-*/":
        numbers.append(int(ch))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            result = operators[ch](first_num, second_num)
            numbers.appendleft(result)

print(int(numbers[0]))