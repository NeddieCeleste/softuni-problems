start_index = int(input())
end_index = int(input())

for index in range(start_index, end_index + 1):
    if index == end_index:
        print(chr(index))
    else:
        print(chr(index), end=' ')