import re, math

f = open('in/2', 'r')
prog = f.read().split(",")
prog = [int(j) for j in prog]
prog_og = prog.copy()

def process(i, ins):
    #print(i, ins)
    if(ins[0] == 1):
        prog[ins[3]] = prog[ins[1]] + prog[ins[2]]
    elif(ins[0] == 2):
        prog[ins[3]] = prog[ins[1]] * prog[ins[2]]
    elif(ins[0] == 99):
        return True
    return False

print(prog)
prog[1] = 12
prog[2] = 2
for i in range(0, len(prog), 4):
    if process(i,  prog[i:i+4]):
        break

print("part1", prog[0])

for j in range(0, 100):
    for k in range(0, 100):
        prog = prog_og.copy()
        prog[1] = j
        prog[2] = k
        for i in range(0, len(prog), 4):
            if process(i,  prog[i:i+4]):
                break
        if prog[0] == 19690720:
            print("part2", (100*j)+k)
        
