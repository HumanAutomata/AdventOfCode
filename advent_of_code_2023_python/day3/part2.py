# this is so scuffed 
# but it works 
# and I want to sleep 
# I'll clean it up tomorrow 


# read file input
# file = open('sample1.txt', 'r')
# file = open('test.txt', 'r')
file = open('input1.txt', 'r')
lines = file.read().splitlines()

# create an empty schematic
rows = cols = len(lines)
schematic = [["." for j in range(cols)] for i in range(rows)]

# create a 2d array copy of lines
trash_lines = [["." for j in range(cols)] for i in range(rows)]
for row in range(0, rows):
    for col in range(0, cols):
        if lines[row][col].isdigit():
            trash_lines[row][col] = lines[row][col]
        if lines[row][col] == '*':
            trash_lines[row][col] = '*'

# print trash lines
for row in range(0, rows):
    for col in range(0, cols):
        print(trash_lines[row][col], end=" ")
    print(end="\n")

gear_locations = []


# copy information into the schematic
# but only keep the gear and numbers
def create_schematic():
    for row in range(0, rows):
        for col in range(0, cols):
            if lines[row][col].isdigit():
                schematic[row][col] = lines[row][col]
            elif lines[row][col] == '*' and is_gear_new(row, col):
                schematic[row][col] = '*'
                gear_locations.append((row, col))


# return true if a '*' is a gear
def print_schematic():
    for row in range(rows):
        for col in range(cols):
            print(schematic[row][col], end=' ')
        print(end='\n')


def is_gear(row, col):
    # if a '*' is adjecent to >= 2 spaces
    # and >= digits, it's a gear
    num_of_spaces = is_adj_to(row, col, '.')
    num_of_digits = 0
    digits = "123456789"
    for digit in digits:
        num_of_digits += is_adj_to(row, col, digit)
    if num_of_spaces >= 2 and num_of_digits >= 2:
        return True
    else:
        return False


def is_gear_new(row, col):
    numbers_found = 0
    numbers = []

    for move, (row_offset, col_offset) in moves.items():
        new_row, new_col = row + row_offset, col + col_offset

        if trash_lines[new_row][new_col].isdigit():
            # we found a digit for the number
            start = trash_lines[new_row][new_col]
            # we will delete digits as we go to avoid overcounting
            trash_lines[new_row][new_col] = 'x'

            # find all the digits to the left
            index = 1
            while 0 <= new_col - index and trash_lines[new_row][new_col - index].isdigit():
                # append at the front
                start = trash_lines[new_row][new_col - index] + start
                trash_lines[new_row][new_col - index] = 'x'
                index += 1

            # find all the digits to the right
            index = 1
            while new_col + index < cols and trash_lines[new_row][new_col + index].isdigit():
                # append at the end
                start = start + trash_lines[new_row][new_col + index]
                trash_lines[new_row][new_col + index] = 'x'
                index += 1

            # we found a number
            numbers_found += 1
            numbers.append(start)

    return True if numbers_found == 2 else False

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


# Return the number of "symbol" adjacent to the cell at (row, col)
def is_adj_to(row, col, symbol):
    count = 0

    for move, (row_offset, col_offset) in moves.items():
        new_row, new_col = row + row_offset, col + col_offset

        if lines[new_row][new_col] == symbol:
            count += 1

    return count


# return all the ratios
def find_ratio(row, col):
    numbers_found = 0
    numbers = []

    while (numbers_found < 2):
        for move, (row_offset, col_offset) in moves.items():
            new_row, new_col = row + row_offset, col + col_offset

            if schematic[new_row][new_col].isdigit():
                # we found a digit for the number
                start = schematic[new_row][new_col]
                # we will delete digits as we go to avoid overcounting
                schematic[new_row][new_col] = 'x'

                # find all the digits to the left
                index = 1
                while (0 <= new_col-index and schematic[new_row][new_col-index].isdigit()):
                    # append at the front
                    start = schematic[new_row][new_col-index] + start
                    schematic[new_row][new_col-index] = 'x'
                    index += 1


                # find all the digits to the right
                index = 1
                while (new_col+index < cols and schematic[new_row][new_col+index].isdigit()):
                    # append at the end
                    start = start + schematic[new_row][new_col+index]
                    schematic[new_row][new_col+index] = 'x'
                    index += 1

                # we found a number
                numbers_found += 1
                numbers.append(start)

            if numbers_found == 2:
                break

    # calculate ratio
    ratio = int(numbers[0]) * int(numbers[1])
    return ratio


total = 0
# find the sum of ratios
create_schematic()
#print("before")
#print_schematic()
#find_ratio(gear_locations[13][0], gear_locations[13][1])

#   
for index, gear in enumerate(gear_locations):
    total += find_ratio(gear[0], gear[1])
    print("progress:", index, "/", len(gear_locations), "subtotal: ", total)
#print("after:")
#print_schematic()
print("Total:", total)
