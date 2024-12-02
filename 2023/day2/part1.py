valid_game = {
    "red": 12,
    "green": 13,
    "blue": 14    
}

def parse_lines(line):
    game_split = line.split(":")
    #game_split[0] = "Game ##"  <- ## is the id 
    game_id = game_split[0][4:]
    grabs = game_split[1].split(";")
    return int(game_id), grabs

def is_game_valid(grabs):
    for grab in grabs:
        cubes = grab.split(",")
        for cube in cubes:
            _, number, colour = cube.split(" ")        
            if int(number) > valid_game[colour]:
                return False
    return True

# read file input 
#file = open('sample1.txt', 'r')
file = open('input1.txt', 'r')
lines = file.read().splitlines()

#sum total
total = 0

for line in lines:
    id, grabs = parse_lines(line)
    if is_game_valid(grabs):
        total += id

#print out total
print(total)



