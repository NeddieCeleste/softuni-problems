n = int(input())
matrix = []

for index in range(n):
    data = [int(x) for x in input().split()]
    matrix.append(data)

diagonal_sum = 0
for row in range(n):
    for col in range(n):
        if row == col:
            diagonal_sum += matrix[row][col]

print(diagonal_sum)