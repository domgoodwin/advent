f = open('inputs/day19.txt', 'r')

grid = []

for line in f:
    grid.append(list(line.replace("\n", "")))

#print(grid)

# 0 is top (y) and left (x)
x,y = 0, 0
# 0 is N, 1 is E, 2 is S, 3 is W
direction = 2
letters = []
at_end = False

def move(cur):
    global grid, x, y, direction, letters, at_end
    if(cur == "|" or cur == "-" or (cur != "+" and cur != " ")):
        print(cur, direction, "-", x, y)
        if(not cur in ["|", "-"]):
            letters.append(cur)
        if(direction == 0):
            y += -1
        elif(direction == 2):
            y += 1
        elif(direction == 1):
            x += 1
        elif(direction == 3):
            x += -1
        else:
            print("Should this happen?", cur, x, y)
    elif(cur == "+"):
        print(cur, direction, "-", x, y)
        # first continue in direction
        nX, nY = x, y
        go = True
        count = 0
        i = direction
        while go:
            nX, nY = x, y
            if(i == 0):
                nY += -1
            elif(i == 1):
                nX += 1
            elif(i == 2):
                nY += 1
            elif(i == 3):
                nX += -1
            #print("Debug",i, nX, nY, "//", cur, x, y, count)
            if(nY < len(grid) and nX < len(grid[nY])  and grid[nY][nX] != " "):
                x, y = nX, nY
                direction = i
                return
            else:
                if(count == 0):
                    i = (direction - 1) % 4
                elif(count == 1):
                    i = (direction + 1) % 4
                else:
                    print("Should this happen?",i, nX, nY, "//", cur, x, y, count)
                    at_end = True
                    return
                count += 1
        
    else:
        print("This shouldn't happen", cur, direction, "-", x, y)
        at_end = True

                


#first line find starting pos 
x = grid[y].index("|")


while(not at_end):
    try:
        cur = grid[y][x]
    except:
        at_end = True
        break
    move(cur)

print(''.join(letters))

    
    

