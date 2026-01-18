odd_set = set()
even_set = set()

for row in range(1, int(input()) +1):
    curr_number = sum(ord(ch) for ch in input()) // row

    if curr_number % 2 == 0:
        even_set.add(curr_number)
    else:
        odd_set.add(curr_number)

if sum(even_set) == sum(odd_set):
    print(", ".join(str(x) for x in even_set | odd_set))
elif sum(odd_set) > sum(even_set):
    print(", ".join(str(x) for x in odd_set - even_set))
else:
    print(", ".join(str(x) for x in even_set ^ odd_set))