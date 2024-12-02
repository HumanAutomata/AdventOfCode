# read file input
# file = open('sample1.txt', 'r')
# file = open('test.txt', 'r')
file = open('input1.txt', 'r')
lines = file.read().splitlines()

star_locations = []
ratios = []

# find the star locations
rows = cols = len(lines)

for row in range(rows):
    for col in range(cols):
        if lines[row][col] == '*':
            star_locations.append((row, col))

# Define the dictionary of moves
moves = {
    'left': (0, -1),
    'right': (0, 1),
    'above': (-1, 0),
    'below': (1, 0),
    'top_left': (-1, -1),
    'top_right': (-1, 1),
    'bottom_left': (1, -1),
    'bottom_right': (1, 1),
}


def find_ratios(row, col):
    # This needs to be a list because otherwise we overcount
    # it works because all the numbers in the input are unique
    # If we don't want to use sets, we can edit the string
    # and write over the numbers we already found,
    # similar to how I was doing before
    numbers = set()

    for move, (row_offset, col_offset) in moves.items():
        new_row, new_col = row + row_offset, col + col_offset

        if lines[new_row][new_col].isdigit():
            # we found a digit for the number
            start = lines[new_row][new_col]

            # find all the digits to the left
            index = 1
            while 0 <= new_col - index and lines[new_row][new_col - index].isdigit():
                # append at the front
                start = lines[new_row][new_col - index] + start
                index += 1

            # find all the digits to the right
            index = 1
            while new_col + index < cols and lines[new_row][new_col + index].isdigit():
                # append at the end
                start = start + lines[new_row][new_col + index]
                index += 1

            # we found a number
            numbers.add(int(start))

    if len(numbers) == 2:
        list_nums = list(numbers)
        ratio = list_nums[0] * list_nums[1]
        ratios.append(ratio)


# find the sum of the ratios
for star in star_locations:
    row = star[0]
    col = star[1]
    find_ratios(row, col)

print("Total:", sum(ratios))
