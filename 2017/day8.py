f = open('inputs/day8.txt', 'r')
# example uz inc 134 if hx > -10
part2 = 0
def mapCon(conL, con, conR):
    if(con == "=="):
        return conL == conR
    if(con == "<"):
        return conL < conR
    if(con == ">"):
        return conL > conR
    if(con == "<="):
        return conL <= conR
    if(con == ">="):
        return conL >= conR
    if(con == "!="):
        return conL != conR

regs = dict()
for line in f:
    ins = line.split(" ")
    #regToMod = line[0: line.find(" ")]
    #mov = line[line.find(" ") + 1:line.find(" ") + 4 ]
    regToMod = ins[0]
    mov = ins[1]
    movVal = int(ins[2])
    conL = ins[4]
    con = ins[5]
    conR = int(ins[6])

    if(not regToMod in regs):
        regs[regToMod] = 0
    if(not conL in regs):
        regs[conL] = 0
    
    if(mapCon(regs[conL], con, conR)):
        if(mov == "inc"):
            regs[regToMod] += movVal
        else:
            regs[regToMod] -= movVal
    for k, v in regs.items():
        if(v > part2):
            part2 = v

part1 = 0
for k, v in regs.items():
    if(v > part1):
        part1 = v

print(part1) 
print(part2)



    