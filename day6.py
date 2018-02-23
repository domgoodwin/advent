f = open('inputs/day6.txt', 'r')

input = f.read().strip()
rawBlocks = input.split("\t")
blocks = [ int(x) for x in rawBlocks ]


def balanceBlocks(blocks, index):
    #print(blocks)
    blocksToRedistribute = blocks[index]
    blocks[index] = 0
    curIndex = index
    while(blocksToRedistribute > 0):
        curIndex += 1
        if(curIndex == len(blocks)): curIndex = 0
        blocks[curIndex] += 1
        blocksToRedistribute -= 1
    return blocks

count = 0
banks = []
curBank = ''.join(str(x) for x in blocks)
while (not curBank in banks):
    banks.append(curBank)
    count += 1
    blocks = balanceBlocks(blocks, blocks.index(max(blocks)))
    curBank = ''.join(str(x) + ',' for x in blocks)
print("PART1")
print(count)

count = 0
banksTwo = []
while (not curBank in banksTwo):
    banksTwo.append(curBank)
    count += 1
    blocks = balanceBlocks(blocks, blocks.index(max(blocks)))
    curBank = ''.join(str(x) + ',' for x in blocks)
print("PART2")
print(count)


