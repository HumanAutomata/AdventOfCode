# read file input
# file = open('sample1.txt', 'r')
file = open('input1.txt', 'r')
lines = file.read().splitlines()

# let's use sets!
winning_numbers = set()
numbers = set()
matches = set()

multiplier = [1] * len(lines)

for index, line in enumerate(lines):
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
    # add new cards
    num_of_cards = len(matches)
    card_index = index + 1
    coefficient = multiplier[index]
    for match in range(num_of_cards):
        multiplier[card_index] += coefficient
        card_index += 1
    # empty the sets
    winning_numbers.clear()
    numbers.clear()
    matches.clear()

print(multiplier)
total = sum(multiplier)
print("Total = %d" % total)
