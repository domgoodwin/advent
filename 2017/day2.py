import re

# get checksum of each line
# each line has tab seperated numbers

f = open('inputs/day2.txt', 'r')

checksums = []
p2sum = 0

for line in f:
    #print line
    numbers = re.split(r'\t+', line)
    highest = 0
    lowest = 0
    tup = ()
    for number in numbers:
        ## part 1
        #print number
        num = int(number)
        if(lowest == 0):
            lowest = num
        if(num < lowest):
            lowest = num
        if(num > highest):
            highest = int(number)


        xnumbers = numbers
        ynumbers = numbers
        for x in xnumbers:
            xNum = int(x)
            yNum = num
            if(((xNum % yNum) == 0) and (xNum != yNum)):
                tup = (xNum, yNum)
    print(tup)
    p2sum += tup[0] / tup[1]



    print("Highest: " + str(highest) + " lowest: " + str(lowest))
    checksums.append(highest - lowest)

checksum = 0
for number in checksums:
    checksum += number

print(checksum)

print("Part 2 total: " + str(p2sum))
