rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    data = [int(y) for y in input().split(", ")]
    matrix.append(data)

max_sum = float("-inf")
sub_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        current = matrix[row][col]
        next_element = matrix[row][col + 1]
        diagonal_element = matrix[row + 1][col + 1]
        below_element = matrix[row + 1][col]

        sum_elements = current + next_element + diagonal_element + below_element
        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [[current, next_element], [below_element, diagonal_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
