file = "./input.txt"

scores = 0
board = []

with open(file) as f:
    for line in f:
        row = [int(x) for x in line.strip()]
        board.append(row)


# maybe this time recursion won't cause me pain
def trailhead_score(row, col, height, found):
    if height == 9:
        # print("reached 9")
        found.add((row, col))

    # up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # try moving to each neighbour
    for direction in directions:

        new_row = row + direction[0]
        new_col = col + direction[1]

        if (
            0 <= new_row < len(board)
            and 0 <= new_col < len(board[0])
            and board[new_row][new_col] == height + 1
        ):

            # print("direction", direction)
            # print(new_row, new_col)
            found = trailhead_score(new_row, new_col, height + 1, found)
            # print("trying")
            # print(new_row, new_col, height + 1, found)

    return found


# for i in range(len(board)):
#     for j in range(len(board[i])):
#         print(board[i][j], end=" ")
#     print()

for i in range(len(board)):
    for j in range(len(board[i])):

        if board[i][j] != 0:
            continue

        score = len(trailhead_score(i, j, 0, set()))
        # print("found", found)
        # print("score", score)
        scores += score


print(scores)
