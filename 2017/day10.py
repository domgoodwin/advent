from operator import xor  
from functools import reduce

f = open('inputs/day10.txt', 'r')

rawIn = f.read()
lengths = [ int(x) for x in rawIn.split(",")]
circle = list(range(0, 256))
curPos = 0
skipSize = 0

## reverse len eles
def knotHashRound(lengths, circle):
    global curPos
    global skipSize
    for le in lengths:
        sb = []
        if((curPos + le) >= 256):
            sb = circle[curPos: 255]
            sb = sb + circle[0: (curPos + le) % 256]
        else:
            sb = circle[curPos: (curPos + le) % 256]

        sb.reverse()
        i = curPos
        for item in sb:
            circle[i] = item
            i = (i + 1) % 256
        curPos = (curPos + le + skipSize) % 256
        skipSize += 1
        #print (circle)
    return circle

oneCircle = knotHashRound(lengths, circle)
#part 1
print(oneCircle[0] * oneCircle[1]) 

#part 2

#convert input to ascii codes
lengths = [ord(x) for x in rawIn.rstrip()] + [17, 31, 73, 47, 23]
print (lengths)
circle = list(range(0, 256))
curPos = 0
skipSize = 0
for i in range(64):
    circle = knotHashRound(lengths, circle)
dense = []
for x in range(0,16):
    subslice = circle[16*x:16*x+16]
    dense.append('%02x'%reduce(xor, subslice))
print(''.join(dense))