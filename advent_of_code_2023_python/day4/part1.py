import math
# read file input
# file = open('sample1.txt', 'r')
file = open('input1.txt', 'r')
lines = file.read().splitlines()

# let's use sets!
winning_numbers = set()
numbers = set()
matches = set()

total = 0

for line in lines:
    _, card = line.split(':')
    winning_numbers_str, numbers_str = card.split('|')
    win_nums = winning_numbers_str.split()
    nums = numbers_str.split()
    # create the winning set
    for num in win_nums:
        winning_numbers.add(int(num))
    # create your set
    for num in nums:
        numbers.add(int(num))
    # find the intersection
    matches = winning_numbers.intersection(numbers)
    # add to the total
    total += math.floor(2 ** (len(matches) - 1))
    # empty the sets
    winning_numbers.clear()
    numbers.clear()
    matches.clear()

print("Total = %d" % total)
