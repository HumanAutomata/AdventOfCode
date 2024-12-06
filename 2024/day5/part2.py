# this took way too long because I was trying to use recursion
# and kept running into infinite loops
# I had to take a step back and eventually figured it out
# technically, still a one-shot

file = "./input1.txt"

sum = 0
all_rules_created = False
rules: dict[int, set] = {}

# there's probably a way to sort based the given rules
# but idk how


def create_rule(line):
    a, b = line.split("|")
    if int(a) not in rules:
        rules[int(a)] = {int(b)}
    else:
        rules[int(a)].add(int(b))


def test_validity(pages):

    prev_pages = {pages[0]}

    for page in pages[1:]:
        if page in rules and rules[page] & prev_pages:
            return False
        prev_pages.add(page)

    return True


def fix_order(pages):
    prev_pages = {pages[0]}

    for i, page in enumerate(pages[1:]):

        if page in rules and rules[page] & prev_pages:

            new_index = i
            numbers = list(rules[page])

            # find the leftmost index
            for number in numbers:
                if number in pages:
                    new_index = min(new_index, pages.index(number))

            # remove the page
            pages.remove(page)
            # add the page back in the correct spot
            pages.insert(new_index, page)
            print(pages)

        prev_pages.add(page)

    return pages


with open(file) as f:
    for line in f:

        if line == "\n":
            all_rules_created = True
            continue

        if not all_rules_created:
            create_rule(line)
            continue

        pages = [int(x) for x in line.split(",")]

        valid = test_validity(pages)

        if not valid:
            print("invaild pages", pages)

            fixed_pages = fix_order(pages)
            print("fixed pages", fixed_pages)
            print()
            sum += fixed_pages[len(fixed_pages) // 2]


print(sum)
