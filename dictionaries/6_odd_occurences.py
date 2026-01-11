elements_count = {}

elements = input().lower()
elements_list = elements.split()
for i in elements_list:
    counted = int(elements_list.count(i))
    elements_count[i] = counted
for key, value in elements_count.items():
    if value % 2 != 0:
        print(f"{key}", end=' ')

