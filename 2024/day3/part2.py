import re

file = "./input1.txt"

product = 0

with open(file) as f:
    contents = f.read()
    instructions = re.findall("do[(][)]|don't[(][)]|mul[(][0-9]+[,][0-9]+[)]", contents)

    enabled = True

    for instruction in instructions:

        if instruction == "do()":
            enabled = True

        elif instruction == "don't()":
            enabled = False

        elif enabled:
            a,b = re.findall("[0-9]+", instruction)
            product += int(a) * int(b)


print(product)


