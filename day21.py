import numpy as np

f = open('inputs/day21.txt', 'r')

en_rules = {}

for line in f:
     rule = line.split(" => ")
     en_rules[rule[0]] = rule[1]

#print(en_rules)


def getSingleUnit(grid):
    #print(grid)
    output = ""
    for row in grid:
        for col in row:
            output += col
        output += "/"
    return output

def getGrid(single):
    grid = []
    cur = []
    for ch in single:
        if(ch=="/"):
            grid.append(cur)
            cur = []
        else:
            cur.append(ch)
    return grid

def getAlts(grid):
    alts = []
    alts.append(grid)
    np_arr = np.array(grid)
    for i in range(0, 4):
        np_arr = np.rot90(np_arr)
        alts.append(np_arr.tolist())
    np_arr = np.array(grid)
    alts.append(np.flip(np_arr, 0))
    alts.append(np.flip(np_arr, 1))
    return [getSingleUnit(a) for a in alts]
    # flip horizontally,vertically
    # rotate 90, 180, 270


#   Starting pattern
#   .#.
#   ..#
#   ###

pat =  [['.', '#', '.'],
        ['.', '.', '#'],
        ['#', '#', '#']]


grids = []


#print(grids)

count = 0
while(count < 1):
    grids = []
    # assumption: list len is always size
    if(len(pat) % 2 == 0):
        for y in range(0, len(pat), 2):
            for x in range(0, len(pat[y]), 2):
                grids.append([
                    [pat[y][x],pat[y][x+1]],
                    [pat[y+1][x],pat[y+1][x+1]]
                    ])
    else:
        for y in range(0, len(pat), 3):
            for x in range(0, len(pat[y]), 3):
                grids.append([
                    [pat[y][x],pat[y][x+1],pat[y][x+2]],
                    [pat[y+1][x],pat[y+1][x+1],pat[y+1][x+2]], 
                    [pat[y+2][x],pat[y+2][x+1],pat[y+2][x+2]]
                    ])
    n_flat_grids = []
    for grid in grids:
        alts = getAlts(grid)
        change = False
        for alt in alts:
            if(alt in en_rules):
                change = True
        n_flat_grids.append(en_rules[getSingleUnit(grid)])
        #if(getSingleUnit(grid) in en_rules):
    # pair back together list of new flats into new pattern

    count += 1

    


