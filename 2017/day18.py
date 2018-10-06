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
ass_code = []
for line in f:
    ins = line.strip().split(" ")
    ass_code.append(ins)

registers = {}
last_sound = 0
i = 0
print(len(ass_code))
while(i < len(ass_code)):
    ins = ass_code[i]
    func, p1 = ins[0], ins[1]
    p2 = ins[2] if len(ins) > 2 else "#"
    if(not p1 in registers):
        registers[p1] = 0
    if(p2 != "#"):        
        try:
            p2 = int(p2)
        except ValueError:
            if(not p2 in registers):
                registers[p2] = 0
            p2 = registers[p2]
    #print(i, ins, registers)
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
        print("part1:", last_sound)
        break
    if(func == "jgz" and registers[p1] > 0):
        i += p2
    else:
        i += 1




# part 2
import threading, time

def send(self_id, p1):
    global prog0, prog1
    if(self_id == 0):
        prog1.rec(p1)
    else:
        prog0.rec(p1)
    


class Program (threading.Thread):
    def __init__(self, id):
        super(Program, self).__init__()
        self.id = id
        self.registers = {}
        self.registers["p"] = id
        self.last_sound = 0
        self.i = 0
        self.recived = []
        self.sent = 0
        self.pause_cond = threading.Condition(threading.Lock())
        self.paused = False
    def rec(self, p1):
        self.recived.append(p1)
    def run(self):
        global ass_code
        print(self.id, "running")
        while(self.i < len(ass_code)):
            ins = ass_code[self.i]
            func, p1 = ins[0], ins[1]
            p2 = ins[2] if len(ins) > 2 else "#"
            if(not p1 in self.registers):
                self.registers[p1] = 0
            if(p2 != "#"):        
                try:
                    p2 = int(p2)
                except ValueError:
                    if(not p2 in self.registers):
                        self.registers[p2] = 0
                    p2 = self.registers[p2]
            #print(self.id, self.i, ins, self.registers)
            if(func == "snd"):
                self.sent += 1
                send(self.id, registers[p1])
            elif(func == "set"):
                self.registers[p1] = p2
            elif(func == "add"):
                self.registers[p1] += p2
            elif(func == "mul"):
                self.registers[p1] = self.registers[p1] * p2
            elif(func == "mod" and p2 != 0):
                self.registers[p1] = self.registers[p1] % p2
            elif(func == "rcv"):
                #print(self.id, self.i, ins, self.registers)
                # get val from queue
                # with self.pause_cond:
                #     while len(self.recived) == 0:
                #         self.pause_cond.acquire()
                #         self.pause_cond.wait()
                #     time.sleep(1)
                if(len(self.recived) == 0):
                    print("waiting",self.id, func, p1, self.registers)
                    self.paused = True
                    time.sleep(1)
                    continue
                self.paused = False
                self.registers[p1] = self.recived.pop(0)

            if(func == "jgz" and self.registers[p1] > 0):
                self.i += p2
            else:
                self.i += 1

# prog0 = Program(0)
# prog1 = Program(1)

prog0 = Program(0)
prog1 = Program(1)
prog0.start()
prog1.start()

while True:
    count = 0
    if(prog0.paused and prog1.paused):
        count += 1
    else:
        count = 0
    if(count > 10):
        print("finished", prog1.sent)
    time.sleep(5)

# prog0.run()
# prog1.run()

prog0.join()
prog1.join()

print(prog1.sent)

#380 too low



    