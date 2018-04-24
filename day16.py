def spin(prog, x):
    end = prog[-x:]
    pr = prog.replace(end, "")
    return end + pr

def exchange(prog, a, b):
    pr = list(prog)
    char = pr[b]
    pr[b] = pr[a]
    pr[a] = char
    return "".join(pr)

def partner(prog, a, b):
    return exchange(prog, prog.index(a), prog.index(b))

#tests
t = "abcdefghijklmnop"
t = spin(t, 2)
assert t == "opabcdefghijklmn"
t = exchange(t, 10, 3)
assert t == "opaicdefghbjklmn"
t = partner(t, "a", "c")
assert t == "opciadefghbjklmn"


def dance(instructions, prog):

    program = prog
    for ins in instructions:
        if(ins[0] == "s"):
            # spin
            program = spin(program, int(ins[1:]))
        elif(ins[0] == "x"):
            # exchanges
            nums = ins[1:].split("/")
            program = exchange(program, int(nums[0]), int(nums[1]))
        elif(ins[0] == "p"):
            # partner
            nums = ins[1:].split("/")
            program = partner(program, nums[0], nums[1])
        else:
            print("This shouldn't happen")
    return program

f = open('inputs/day16.txt', 'r')
instructions = ""
for line in f:
    instructions = line.split(",")


program = "abcdefghijklmnop"
#part 1
print(dance(instructions, program))

#part 2
# 1bil is too many, if program repeats stop it
variations = []
index = 0
for i in range(0, 1000000000):
    program = dance(instructions, program)
    if(program in variations):
        print(i)
        index = i
        break
    variations.append(program)

program = variations[1000000000 % index - 1]
print(program)