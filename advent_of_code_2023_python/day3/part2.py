# read file input
# file = open('sample1.txt', 'r')
# file = open('test.txt', 'r')
file = open('input1.txt', 'r')
lines = file.read().splitlines()

gear_locations = []
star_locations = []
total_ratios = []

# create an empty schematic
rows = cols = len(lines)
schematic = [["." for j in range(cols)] for i in range(rows)]

# create a 2d array copy of lines
# and find the star locations
schematic = [["." for j in range(cols)] for i in range(rows)]
for row in range(0, rows):
    for col in range(0, cols):
        if lines[row][col].isdigit():
            schematic[row][col] = lines[row][col]
        if lines[row][col] == '*':
            schematic[row][col] = '*'
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


# return true if a '*' is a gear
def print_schematic():
    for row in range(rows):
        for col in range(cols):
            print(schematic[row][col], end=' ')
        print(end='\n')


def is_gear_new(row, col):
    numbers_found = 0
    numbers = []

    for move, (row_offset, col_offset) in moves.items():
        new_row, new_col = row + row_offset, col + col_offset

        if schematic[new_row][new_col].isdigit():
            # we found a digit for the number
            start = schematic[new_row][new_col]
            # we will delete digits as we go to avoid overcounting
            schematic[new_row][new_col] = 'x'

            # find all the digits to the left
            index = 1
            while 0 <= new_col - index and schematic[new_row][new_col - index].isdigit():
                # append at the front
                start = schematic[new_row][new_col - index] + start
                schematic[new_row][new_col - index] = 'x'
                index += 1

            # find all the digits to the right
            index = 1
            while new_col + index < cols and schematic[new_row][new_col + index].isdigit():
                # append at the end
                start = start + schematic[new_row][new_col + index]
                schematic[new_row][new_col + index] = 'x'
                index += 1

            # we found a number
            numbers_found += 1
            numbers.append(start)

    if numbers_found == 2:
        ratio = int(numbers[0]) * int(numbers[1])
        total_ratios.append(ratio)
        return True
    else:
        return False


def find_gears():
    for star in star_locations:
        row = star[0]
        col = star[1]
        is_gear_new(row, col)


# find the sum of ratios
find_gears()
print("Total:", sum(total_ratios))
