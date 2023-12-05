# read file input
# file = open('sample1.txt', 'r')
file = open('input1.txt', 'r')
lines = file.read().splitlines()

# we are going to pad the outer layer of the schematic
input_rows = input_cols = len(lines)

rows = input_rows + 2
cols = input_cols + 2

# create an empty schematic
schematic = [["." for j in range(cols)] for i in range(rows)]

# list of symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+', '/']

digits = ""
digit_locations = ""

# copy information into the schematic
# and find all the digits
for row in range(0, input_rows):
    for col in range(0, input_cols):
        if lines[row][col].isdigit():
            schematic[row+1][col+1] = lines[row][col]
            digits += lines[row][col]
            digit_locations += str(row) + ',' + str(col) + "|"

        elif lines[row][col] in symbols:
            schematic[row+1][col+1] = '#'
            digits += " "
            digit_locations += " "
        else:
            digits += " "
            digit_locations += " "

# construct numbers and their locations
numbers = digits.split()
number_locations = digit_locations.split()


# unpacks the number_locations from "0,0|0,1|0,2|" to [(0,0), (0,1), (0,2)]
def unpack_locations(str_location):
    coordinates = []
    str_coordinates = str_location[:-1].split('|')
    for str_coordinate in str_coordinates:
        coordinate = str_coordinate.split(',')
        x = coordinate[0]
        y = coordinate[1]
        coordinates.append((x, y))
    return coordinates


# function to calculate if a number is a "part number"
def is_part_number(location):
    coordinates = unpack_locations(location)
    for coordinate in coordinates:
        # remember we padded the schematic
        row = int(coordinate[0]) + 1
        col = int(coordinate[1]) + 1
        # check to the left
        if schematic[row-1][col] in symbols:
            return True
        # check to the right
        elif schematic[row+1][col] in symbols:
            return True
        # check to the above
        elif schematic[row][col-1] in symbols:
            return True
        # check to the below
        elif schematic[row][col+1] in symbols:
            return True
        # check top-left diagonal
        elif schematic[row - 1][col - 1] in symbols:
            return True
        # check top-right diagonal
        elif schematic[row - 1][col + 1] in symbols:
            return True
        # check bottom-left diagonal
        elif schematic[row + 1][col - 1] in symbols:
            return True
        # check bottom-right diagonal
        elif schematic[row + 1][col + 1] in symbols:
            return True
    return False


total = 0
# find the part numbers
for index, number in enumerate(numbers):
    if is_part_number(number_locations[index]):
        total += int(number)

print("Total:", total)
