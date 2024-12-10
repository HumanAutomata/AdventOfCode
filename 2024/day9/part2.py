file = "./input.txt"

checksum = 0

""" get input """

with open(file) as f:
    input = f.read().strip()

blocks = []

space = False
id = 0

for char in input:
    if space:
        spaces = "." * int(char)
        blocks += spaces
        space = False
    else:
        for _ in range(int(char)):
            blocks.append(id)

        id += 1
        space = True

""" do the shuffing """

moved = set()

def move(block_start_index, block_id, block_size, end_index):

    index = 0
    while index <= end_index:

        # ignore other blocks
        if blocks[index] != ".":
            index += 1
            continue

        # find the space
        start_index = index
        space_size = 1
        index += 1
        while blocks[index] == ".":
            space_size += 1
            index += 1

        # can't fit
        if space_size < block_size:
            index += 1
            continue

        # replace
        for i in range(block_size):
            blocks[start_index + i] = block_id
            blocks[block_start_index - i] = "."
        break



index = len(blocks) - 1
while index >= 0:

    # get the block
    if blocks[index] not in moved:
        block_start_index = index
        block_id = blocks[index]
        block_size = 1
        index -= 1
        while blocks[index] == block_id:
            block_size += 1
            index -= 1
        # try moving it
        move(block_start_index, block_id, block_size, index)
        moved.add(block_id)

    else:
        index -= 1


""" print results """

for i, num in enumerate(blocks):
    if num == ".":
        continue
    checksum += i * int(num)

print(checksum)
