n_rows, n_cols = [int(x) for x in input().split(", ")]
matrix = []

for i in range(n_rows):
    data = [int(x) for x in input().split()]
    matrix.append(data)

for col in range(n_cols):
    col_sum = 0
    for row in range(n_rows):
        col_sum += matrix[row][col]
    print(col_sum)