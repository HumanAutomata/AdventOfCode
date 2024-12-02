# read file input
file = open('sample1.txt', 'r')
# file = open('input1.txt', 'r')
lines = file.read().splitlines()

# sum total
total = 0

for line in lines:
    digits = ""
    for char in line:
        if char.isnumeric():
            digits += char
    # concatonate first and last digit and add to total
    line_total = digits[0] + digits[-1]
    total += int(line_total)

# print out total
print(total)
