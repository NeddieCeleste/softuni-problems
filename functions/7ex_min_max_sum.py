def min_number(num) -> int:
    return min(num)

def max_number(num) -> int:
    return max(num)

def sum_number(num) -> int:
    return sum(num)

numbers = list(map(int, input().split()))
print(f"The minimum number is {min_number(numbers)}")
print(f"The maximum number is {max_number(numbers)}")
print(f"The sum number is: {sum_number(numbers)}")