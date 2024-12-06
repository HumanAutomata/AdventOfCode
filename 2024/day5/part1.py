file = "./input1.txt"

sum = 0
all_rules_created = False
rules: dict[int, set] = {}


def create_rule(line):
    a, b = line.split("|")
    if int(a) not in rules:
        rules[int(a)] = {int(b)}
    else:
        rules[int(a)].add(int(b))


def test_validity(line):
    pages = [int(x) for x in line.split(",")]
    middle = pages[len(pages) // 2]

    prev_pages = {pages[0]}

    for page in pages[1:]:
        if page in rules and rules[page] & prev_pages:
            return 0
        prev_pages.add(page)

    return middle


with open(file) as f:
    for line in f:

        if line == "\n":
            all_rules_created = True
            continue

        if not all_rules_created:
            create_rule(line)
            continue

        sum += test_validity(line)

print(sum)
