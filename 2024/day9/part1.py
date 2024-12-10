file = "./input.txt"

checksum = 0

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

        # block = id * int(char)
        # blocks += block
        id += 1
        space = True

index = 0
while index < len(blocks):
    # trim spaces
    while blocks[-1] == ".":
        del blocks[-1]

    # replace any intermediate space
    if blocks[index] == ".":
        blocks[index] = blocks[-1]
        del blocks[-1]

    index += 1

for i, num in enumerate(blocks):
    checksum += i * int(num)

print(checksum)
