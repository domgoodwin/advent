f = open('inputs/day11.txt', 'r')

# north, northeast, southeast, south, southwest, and northwest:

#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \

rawin = f.read()

#even row left shifted
#odd row right shifted
location = [0,0,0]

instructions = rawin.split(",")
distances = []

def calcDist(loc):
    return (abs(loc[0]) + abs(loc[1]) + abs(loc[2])) / 2

def shiftLocation(x, y, z):
    global location, distances
    location = [location[0] + x, location[1] + y, location[2] + z]
    distances.append(calcDist(location))

def move(instruction):
    if(instruction == "n"):
        shiftLocation(0, 1, -1)
    if(instruction == "ne"):
        shiftLocation(1, 0, -1)
    if(instruction == "se"):
        shiftLocation(1, -1, 0)
    if(instruction == "s"):
        shiftLocation(0, -1, 1)
    if(instruction == "sw"):
        shiftLocation(-1, 0, 1)
    if(instruction == "nw"):
        shiftLocation(-1, 1, 0)


for instruction in instructions:
    move(instruction)

print(calcDist(location))
print(max(distances))


