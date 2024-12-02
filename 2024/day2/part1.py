file = "./input1.txt"

safe = 0

with open(file) as f:
    for line in f:
        levels = [int(x) for x in line.split()]

        if sorted(levels) == levels or sorted(levels, reverse=True) == levels:

            failed = False
            prev = levels[0]

            for i in range(1, len(levels)):
                if levels[i] == prev or abs(levels[i] - prev) > 3:
                    failed = True
                    break
                prev = levels[i]

            safe += 0 if failed else 1


print(safe)
