import itertools

calibration = 0

file = "./input.txt"


def check(result, numbers):
    num_of_ops = len(numbers) - 1
    combinations = list(itertools.product(["+", "*", "||"], repeat=num_of_ops))

    for combinaton in combinations:

        ops = list(combinaton)
        op_index = 0
        total = numbers[0]

        for number in numbers[1:]:

            # perform the calculation
            if ops[op_index] == "+":
                total += number
            elif ops[op_index] == "*":
                total *= number
            else:
                total = int(str(total) + str(number))

            op_index += 1

            if total > result:
                break

        if total == result:
            return result

    return 0


with open(file) as f:
    for line in f:

        result, numbers = line.split(":")
        result = int(result)
        numbers = [int(x) for x in numbers.split()]

        calibration += check(result, numbers)


print(calibration)
