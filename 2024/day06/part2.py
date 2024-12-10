"""
the smart way to do this is to place the new obsticle so that it forms a rectacle with 3 existing ones

for example:
.#....
.....#
.^....
O.....
....#.

but I have a dinner to go to, so maybe we just try every single placement. It can't be that slow, right? RIGHT?

well, 1m52. It's so dumb, but it works!

"""

import copy  # cause curr_board = board doesn't work :(

file = "./input1.txt"

# 10, 130
width = 130

pad = ["$" for _ in range(width + 2)]

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


def move(pos, direction, board):

    move = moves[direction]
    next_pos = (pos[0] + move[0], pos[1] + move[1])

    # if you hit an obsticle
    if board[next_pos[0]][next_pos[1]] in "#O":

        # turn
        direction = (direction + 1) % 4

        return pos, direction

    return next_pos, direction


def patrol(start_row, start_col, board):

    pos = (start_row, start_col)
    direction = 0
    found = [pos]

    while board[pos[0]][pos[1]] != "$":
        # mark the cell as found
        found.append(pos)
        board[pos[0]][pos[1]] = "X"

        # do the next move
        pos, direction = move(pos, direction, board)

        # if this is really dumb
        if len(found) > width * len(board):
            return 1

    return 0


def find_loops(start_row, start_col, board):

    positions = 0

    for i in range(1, width + 1):
        for j in range(1, len(board)):

            # only test available spots
            if board[i][j] != ".":
                continue

            # reset board
            curr_board = copy.deepcopy(board)

            # try adding an obsticle
            curr_board[i][j] = "O"

            loop = patrol(start_row, start_col, curr_board)

            if loop:
                # print("pos", i, j)
                positions += 1

    return positions


print(find_loops(start_row, start_col, board))
