"""
[x] read in all the input
[x] create a dictionary to hold all the positions each antenna is located at
[x] for each type of antenna, create all possible pairs
[x] iterate through all possible pairs and calculate their line (slope)
[x] try to place a # at the two locations (antenna +/- slope)
6. if not out of bounds, add the location to a set
7. print len of set
"""

import itertools

file = "./input.txt"

antennae = {}
antinodes = set()
row = 0
col = 0


with open(file) as f:
    for line in f:

        line = list(line.strip())
        col = len(line)

        for char in line:
            if char != ".":
                if char in antennae:
                    antennae[char] += [(row, line.index(char))]
                else:
                    antennae[char] = [(row, line.index(char))]

        row += 1


def is_valid(curr_row, curr_col):
    if (0 <= curr_row < row) and (0 <= curr_col < col):
        return True
    else:
        return False


for key in antennae:
    possible_pairs = list(itertools.combinations(antennae[key], 2))

    for pairs in possible_pairs:
        row1, col1 = int(pairs[0][0]), int(pairs[0][1])
        row2, col2 = int(pairs[1][0]), int(pairs[1][1])
        row_slope, col_slope = row2 - row1, col2 - col1

        # antennae themselves are automatically counted
        antinodes.add((row1, col1))
        antinodes.add((row2, col2))

        # check up
        while True:
            row_node, col_node = row1 - row_slope, col1 - col_slope

            if is_valid(row_node, col_node):
                antinodes.add((row_node, col_node))
                row1 = row_node
                col1 = col_node
            else:
                break

        # check down
        while True:
            row_node, col_node = row2 + row_slope, col2 + col_slope
            if is_valid(row_node, col_node):
                antinodes.add((row_node, col_node))
                row2 = row_node
                col2 = col_node
            else:
                break


print("Number of antinodes:", len(antinodes))
