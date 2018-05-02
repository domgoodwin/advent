f = open('inputs/day23.txt', 'r')
code = []
for line in f:
    ins = line.strip().split(" ")
    code.append(ins)

import re
def get(p):   
    r = 0
    try:
        r = int(p)
    except ValueError:
        r = regs[p]
    return r

part1 = 0
#print(code)
regs = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0}
i = 0
while(i<len(code)):
    f, p1, pa2 = code[i]
    print(code[i], i)
    p2 = get(pa2)
    if(f == "set"):
        regs[p1] = p2
    elif(f == "sub"):
        regs[p1] -= p2
    elif(f == "mul"):
        part1 += 1
        regs[p1] *= p2
    if(f == "jnz" and get(p1) != 0):
        i += p2
    else:
        i += 1
        
print("part1", part1)
