import re

file = "./input1.txt"

product = 0

with open(file) as f:
    contents = f.read()
    # don't call me cheap - this is my first time using regex in python
    instructions = re.findall("mul[(][0-9]+[,][0-9]+[)]", contents)

    for mul in instructions:
        a,b = re.findall("[0-9]+", mul)
        product += int(a) * int(b)


print(product)


