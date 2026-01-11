def sorted_numbers(num: list) -> list:
    return sorted(num, key = int)

numbers = input().split()
sorted_final = sorted_numbers(numbers)
print("[" + ", ".join(sorted_final) + "]")