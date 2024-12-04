file = "./sample1.txt"

count = 0
# 10, 140
WIDTH = 10

# create a 2D array to store the board
# pad the edges so that we don't have to deal with edge cases

empty_row = ["*" for _ in range(3 + WIDTH + 3)]

board = [empty_row, empty_row, empty_row]


with open(file) as f:
    for line in f:
        row = "***" + line[:-1] + "***"
        board.append(list(row))


for _ in range(4):
    board.append(empty_row)

# for row in board:
#     print(row)


def check(a, b):
    local_count = 0
    # down
    word = board[a][b] + board[a + 1][b] + board[a + 2][b] + board[a + 3][b]
    local_count += int(word == "XMAS")
    # up
    word = board[a][b] + board[a - 1][b] + board[a - 2][b] + board[a - 3][b]
    local_count += int(word == "XMAS")
    # left
    word = board[a][b] + board[a][b + 1] + board[a][b + 2] + board[a][b + 3]
    local_count += int(word == "XMAS")
    # right
    word = board[a][b] + board[a][b - 1] + board[a][b - 2] + board[a][b - 3]
    local_count += int(word == "XMAS")
    # diagonal up left
    word = board[a][b] + board[a - 1][b - 1] + board[a - 2][b - 2] + board[a - 3][b - 3]
    local_count += int(word == "XMAS")
    # diagonal up right
    word = board[a][b] + board[a - 1][b + 1] + board[a - 2][b + 2] + board[a - 3][b + 3]
    local_count += int(word == "XMAS")
    # diagonal down left
    word = board[a][b] + board[a + 1][b + 1] + board[a + 2][b + 2] + board[a + 3][b + 3]
    local_count += int(word == "XMAS")
    # diagonal down righ
    word = board[a][b] + board[a + 1][b - 1] + board[a + 2][b - 2] + board[a + 3][b - 3]
    local_count += int(word == "XMAS")

    return local_count


for i in range(0 + 3, WIDTH + 3):
    for j in range(0 + 3, len(board) - 3):
        if board[i][j] == "X":
            count += check(i, j)


print(f"count: {count}")
