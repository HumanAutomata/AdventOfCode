# row, col and x,y are backwards
# so I'm just gonna just stick with row, col


file = "./input1.txt"

# 10, 130
padding_width = 10

pad = ["$" for _ in range(10 + 2)]

board = [pad]

start_found = False

# one indexed since we pad
start_row = 1
start_col = 1

with open(file) as f:
    for line in f:

        if "^" in line:
            start_col += line.index("^")
            start_found = True

        if not start_found:
            start_row += 1

        row = "$" + line.strip() + "$"
        board.append(list(row))


board.append(pad)


# I think you are supposed to use enums for this
# remember: (row, col)
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

moves = [UP, RIGHT, DOWN, LEFT]


def move(pos, direction):

    move = moves[direction]
    next_pos = (pos[0] + move[0], pos[1] + move[1])

    if board[next_pos[0]][next_pos[1]] == "#":
        direction = (direction + 1) % 4
        return pos, direction

    return next_pos, direction


def patrol(start_row, start_col):

    pos = (start_row, start_col)
    direction = 0
    found = {pos}

    while board[pos[0]][pos[1]] != "$":
        # mark the cell as found
        found.add(pos)
        # board[pos[0]][pos[1]] = "X"

        # print('pos', pos)
        # for row in board:
        #     print(row)


        # do the next move
        pos, direction = move(pos, direction)

    print(len(found))


patrol(start_row, start_col)
