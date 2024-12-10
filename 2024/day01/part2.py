file = "./input1.txt"

list1 = []
list2:dict[int, int] = {}

with open(file) as f:
    for line in f:
        a_str, b_str = line.split()
        a = int(a_str)
        b = int(b_str)

        list1.append(a)
        if b not in list2:
            list2[b] = 1
        else:
            list2[b] += 1


score = 0

for value in list1:
    if value in list2:
        score += value * list2[value]


print(score)
