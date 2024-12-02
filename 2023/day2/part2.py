min_number = {
    "red": 0,
    "green": 0,
    "blue": 0    
}

def parse_lines(line):
    _, games = line.split(":")
    grabs = games.split(";")
    return grabs

def calculate_power(grabs):
    for grab in grabs:
        cubes = grab.split(",")
        for cube in cubes:
            _, number, colour = cube.split(" ")        
            min_number[colour] = max(int(number), min_number[colour])
    power = min_number["blue"] * min_number["green"] * min_number["red"]
    min_number["blue"] = min_number["green"] = min_number["red"] = 0
    return power



# read file input 
#file = open('sample1.txt', 'r')
file = open('input1.txt', 'r')
lines = file.read().splitlines()

#sum total
total = 0

for line in lines:
    grabs = parse_lines(line)
    total += calculate_power(grabs)            

#print out total
print(total)



