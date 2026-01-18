n_rows, n_cols = [int(x) for x in input().split(", ")]

total = 0
matrix = []

for _ in range(n_rows):
    data = [int(y) for y in input().split(", ")]
    matrix.append(data)
    total += sum(data)

print(total)
print(matrix)