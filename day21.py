import numpy as np
import math

f = open('inputs/day21.txt', 'r')

en_rules = {}

for line in f:
     rule = line.split(" => ")
     en_rules[rule[0]] = rule[1].strip()

#print(en_rules)


def getSingleUnit(grid):
    #print(grid)
    output = ""
    for row in grid:
        for col in row:
            output += col
        output += "/"
    return output[:len(output) - 1]

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
    fl0 = np.flip(np_arr, 0)
    fl1 = np.flip(np_arr, 1)
    alts.append(fl0.tolist())
    alts.append(fl1.tolist())
    np_arr = np.array(grid)
    for i in range(0, 4):
        np_arr = np.rot90(np_arr)
        alts.append(np_arr.tolist())
    for i in range(0, 4):
        fl0 = np.rot90(fl0)
        alts.append(fl0.tolist())
    for i in range(0, 4):
        fl1 = np.rot90(fl1)
        alts.append(fl1.tolist())
    return [getSingleUnit(a) for a in alts]
    # flip horizontally,vertically
    # rotate 90, 180, 270

def getCount(f_pat):
    # if "" count all
    count = 0
    for flat in f_pat:
        n = flat.strip().replace("/","")
        count += len(n)
    return count

#   Starting pattern
#   .#.
#   ..#
#   ###

pat =  [['.', '#', '.'],
        ['.', '.', '#'],
        ['#', '#', '#']]

# pat =  [['.', '#', '.','.', '.', '#'],
#         ['.', '.', '#','#', '#', '.'],
#         ['#', '#', '#','.', '#', '.'],
#         ['#', '#', '.','#', '.', '#'],
#         ['.', '.', '#','#', '#', '.'],
#         ['#', '#', '#','.', '.', '#']]


grids = []


#print(grids)
print(en_rules)
count = 0

while(count < 5):
    print("before", pat)
    g_size = 0
    size = len(pat)
    grids = []
    # assumption: list len is always size
    if(len(pat) % 2 == 0):
        g_size = 2
        for y in range(0, len(pat), 2):
            for x in range(0, len(pat[y]), 2):
                grids.append([
                    [pat[y][x],pat[y][x+1]],
                    [pat[y+1][x],pat[y+1][x+1]]
                    ])
    else:
        g_size = 3
        for y in range(0, len(pat), 3):
            for x in range(0, len(pat[y]), 3):
                grids.append([
                    [pat[y][x],pat[y][x+1],pat[y][x+2]],
                    [pat[y+1][x],pat[y+1][x+1],pat[y+1][x+2]], 
                    [pat[y+2][x],pat[y+2][x+1],pat[y+2][x+2]]
                    ])
    #print(grids)
    n_flat_grids = []
    for grid in grids:
        alts = getAlts(grid)
        change = ""
        for alt in alts:
            print(alt)
            if(alt in en_rules):
                change = alt
                print(alt, change, "!!")
                break
        if(change != ""):
            print("making a change", change)
            n_flat_grids.append(en_rules[change].strip())
        else:
            n_flat_grids.append(getSingleUnit(grid).strip())
        change = ""
    print(n_flat_grids)
    # pair back together list of new flats into new pattern
    i = 0
    rg = 0
    n_pat = []
    # find out size of whole new grid
    
    t_count = getCount(n_flat_grids)
    g_len = int(math.sqrt(t_count))
    for i in range(0, g_len): # col count
        n_pat.append([])
    #print(n_pat)
    row = 0 #  0 is top row, 1 is down one
    col = 0 # 0 is leftmost
    for grid in n_flat_grids:
        
        items = grid.strip().split("/")
        if(col >= g_len):
            col = 0
            row += len(items[0])

        i = 0
        for item in items:
            #print(row, col, i)
            for ch in item:
                n_pat[row + i].append(ch)
            i += 1
        col += len(items[0])
    
    print("after",n_pat)
    pat = n_pat
    # list will be top row, LEFT TO RIGHT, then next row (block)
    count += 1

on_count = 0
for row in pat:
    for ch in row:
        on_count += 1 if ch == "#" else 0
print("part1", on_count)

    


