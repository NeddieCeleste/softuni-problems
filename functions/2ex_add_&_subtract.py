def sum_numbers(first: int, second: int) -> int:
    return first + second

def subtract(some_result: int, third: int) -> int:
    return some_result - third

def add_and_subtract(int1: int, int2: int, int3: int) -> int:
    returned_result = sum_numbers(int1, int2)
    final_result = subtract(returned_result, int3)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = add_and_subtract(first_number, second_number, third_number)
print(result)
