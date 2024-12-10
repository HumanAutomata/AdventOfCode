file = "./input1.txt"

safe = 0


def is_safe_ascending(levels):
    prev = levels[0]
    for i in range(1, len(levels)):
        if not (0 < levels[i] - prev < 4):
            return 0
        prev = levels[i]

    return 1


def ascending(levels):

    prev = levels[0]
    for i in range(1, len(levels)):
        if 0 < levels[i] - prev < 4:
            prev = levels[i]
        else:
            # there's probably a smart way to figure out which value to remove
            # but I'm not feeling that smart right now

            # remove the current value and try again
            list1 = levels[0:i] + levels[i + 1 :]
            res1 = is_safe_ascending(list1)

            # remove the prev value and try again
            list2 = levels[0 : i - 1] + levels[i:]
            res2 = is_safe_ascending(list2)

            return max(res1, res2)

    return 1


def is_safe_descending(levels):
    prev = levels[0]
    for i in range(1, len(levels)):
        if not (0 < prev - levels[i] < 4):
            return 0
        prev = levels[i]

    return 1


def descending(levels):

    prev = levels[0]
    for i in range(1, len(levels)):
        if 0 < prev - levels[i] < 4:
            prev = levels[i]

        else:
            # remove the current value and try again
            list1 = levels[0:i] + levels[i + 1 :]
            res1 = is_safe_descending(list1)

            # remove the prev value and try again
            list2 = levels[0 : i - 1] + levels[i:]
            res2 = is_safe_descending(list2)

            return max(res1, res2)

    return 1


with open(file) as f:
    for line in f:
        levels = [int(x) for x in line.split()]
        safe += max(ascending(levels), descending(levels))


print(safe)
