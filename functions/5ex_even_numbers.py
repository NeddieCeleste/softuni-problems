def is_even(number) -> bool:
    return number % 2 == 0

numbers_as_string = input().split()
numbers_as_digits = []
for numbers in numbers_as_string:
    numbers_as_digits.append(int(numbers))

result = list(filter(is_even, numbers_as_digits))
print(result)