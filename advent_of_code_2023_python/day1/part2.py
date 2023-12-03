# read file input 
#file = open('sample1.txt', 'r')
file = open('input1.txt', 'r')
lines = file.read().splitlines()

#sum total
total = 0

#dictionaries 
three_letter_digits = {
    'one': '1',
    'two': '2',
    'six': '6'
}

four_letter_digits = {
    'four': '4',
    'five': '5',
    'nine': '9'
}

five_letter_digits = {
    'three': '3',
    'seven': '7',
    'eight': '8'
}

for line in lines:
    digits = "" 
    for index, char in enumerate(line):
        # if char is a digit
        if char.isnumeric():
            digits += char
        # if there's a 3 letter digit
        elif line[index:index+3] in three_letter_digits:
            key = line[index:index+3]
            digits += three_letter_digits[key]
            index+=3    
        # if there's a 4 letter digit 
        elif line[index:index+4] in four_letter_digits:
            key = line[index:index+4]
            digits += four_letter_digits[key] 
            index+=4    
        # if there's a 5 letter digit
        elif line[index:index+5] in five_letter_digits:
            key = line[index:index+5] 
            digits += five_letter_digits[key] 
            index+=5 
   
    # concatonate first and last digit and add to total
    line_total = digits[0] + digits[-1]
    total += int(line_total)

#print out total
print(total)



