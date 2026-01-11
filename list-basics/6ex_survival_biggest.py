integer_list = []
numbers = input().split(" ")
n = int(input())
for index in numbers:
    number_values = index.split(" ")
    integer_list.append(int(number_values[0]))
for removed in range(n):
    integer_list.remove(min(integer_list))


print(", ".join(map(str, integer_list)))
