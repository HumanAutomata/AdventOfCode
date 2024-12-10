file = "./input1.txt"

list1 = []
list2 = []

with open(file) as f:
    for line in f:
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))


list1.sort()
list2.sort()

sum = 0

for i in range(0, len(list1)):
    sum += abs(list1[i] - list2[i])

print(sum)
