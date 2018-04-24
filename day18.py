# snd X plays a sound with a frequency equal to the value of X.
# set X Y sets register X to the value of Y.
# add X Y increases register X by the value of Y.
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
# mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
# rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
# jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

#It seems like the assembly is meant to operate on a set of registers that are each named with a single letter and that can each hold a single integer. 
# You suppose each register should start with a value of 0.

#Many of the instructions can take either a register (a single letter) or a number. The value of a register is the integer it contains; the value of a number is that number.
#After each jump instruction, the program continues with the instruction to which the jump jumped. 
# After any other instruction, the program continues with the next instruction. Continuing (or jumping) off either end of the program terminates it.
f = open('inputs/day18.txt', 'r')

registers = {}
last_sound = 0
ass_code = []
for line in f:
    ins = line.strip().split(" ")
    ass_code.append(ins)

i = 0
print(len(ass_code))
while(i < len(ass_code)):
    ins = ass_code[i]
    func, p1 = ins[0], ins[1]
    p2 = ins[2] if len(ins) > 2 else "#"
    #print(func, p1, p2)
    # if not in dict init
    if(not p1 in registers):
        registers[p1] = 0
    if(p2 != "#"):        
        try:
            p2 = int(p2)
        except ValueError:
            if(not p2 in registers):
                registers[p2] = 0
            p2 = registers[p2]
    print(i, ins, registers)
    if(func == "snd"):
        last_sound = registers[p1]
    elif(func == "set"):
        registers[p1] = p2
    elif(func == "add"):
        registers[p1] += p2
    elif(func == "mul"):
        registers[p1] = registers[p1] * p2
    elif(func == "mod" and p2 != 0):
        registers[p1] = registers[p1] % p2
    elif(func == "rcv"):
        print(last_sound)
        break
    if(func == "jgz" and registers[p1] > 0):
        i += p2
    else:
        i += 1



    