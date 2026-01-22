m_presents = int(input())
n_size = int(input())

matrix = []
santa_pos = []
nice_kids_total = 0
nice_kids_gifted = 0

for r in range(n_size):
    row_data = input().split()
    matrix.append(row_data)
    if "S" in row_data:
        santa_pos = [r, row_data.index("S")]
    nice_kids_total += row_data.count("V")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()

while command != "Christmas morning":
    curr_r, curr_c = santa_pos
    move_r, move_c = directions[command]
    next_r, next_c = curr_r + move_r, curr_c + move_c

    if 0 <= next_r < n_size and 0 <= next_c < n_size:
        matrix[curr_r][curr_c] = "-"

        if matrix[next_r][next_c] == "V":
            m_presents -= 1
            nice_kids_gifted += 1

        elif matrix[next_r][next_c] == "C":
            for d_r, d_c in directions.values():
                near_r, near_c = next_r + d_r, next_c + d_c

                if matrix[near_r][near_c] in ["V", "X"]:
                    if matrix[near_r][near_c] == "V":
                        nice_kids_gifted += 1
                    m_presents -= 1
                    matrix[near_r][near_c] = "-"

                    if m_presents == 0:
                        break

        matrix[next_r][next_c] = "S"
        santa_pos = [next_r, next_c]

    if m_presents <= 0:
        break

    command = input()

if m_presents == 0 and nice_kids_gifted < nice_kids_total:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]

if nice_kids_gifted == nice_kids_total:
    print(f"Good job, Santa! {nice_kids_total} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_total - nice_kids_gifted} nice kid/s.")