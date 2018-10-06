input = "stpzcrnm"



## reverse len eles
def knotHashRound(lengths, circle):
    curPos = 0
    skipSize = 0
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

