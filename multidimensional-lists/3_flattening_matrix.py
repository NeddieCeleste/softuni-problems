n = int(input())
matrix = []

for _ in range(n):
    data = [int(x) for x in input().split(", ")]
    matrix.extend(data)

print(matrix)
