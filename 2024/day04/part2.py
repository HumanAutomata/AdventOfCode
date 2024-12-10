file = "./input1.txt"

count = 0
# 10, 140
WIDTH = 140

# create a 2D array to store the board
# pad the edges so that we don't have to deal with edge cases

empty_row = ["." for _ in range(3 + WIDTH + 3)]

board = [empty_row, empty_row, empty_row]


with open(file) as f:
    for line in f:
        row = "..." + line[:-1] + "..."
        board.append(list(row))


for _ in range(4):
    board.append(empty_row)

# valid x-shapes flattened into sequences
# 4 possible rotations
valid_sequences = ["MSAMS", "MMASS", "SMASM", "SSAMM"]


for i in range(0 + 3, WIDTH + 3):
    for j in range(0 + 3, len(board) - 3):

        if board[i][j] == "M" or board[i][j] == "S":
            top_left = board[i][j]
            top_right = board[i][j + 2]
            center = board[i + 1][j + 1]
            bottom_left = board[i + 2][j]
            bottom_right = board[i + 2][j + 2]

            sequence = top_left + top_right + center + bottom_left + bottom_right

            count += int(sequence in valid_sequences)



print(f"count: {count}")
