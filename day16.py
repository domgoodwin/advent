f = open('inputs/day16.txt', 'r')

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
    print(prog, a, b, prog.index(a), prog.index(b))
    return exchange(prog, prog.index(a), prog.index(b))

#tests
t = "abcdefghijklmnop"
t = spin(t, 2)
print(t)
assert t == "opabcdefghijklmn"
t = exchange(t, 10, 3)
print(t)
assert t == "opaicdefghbjklmn"
t = partner(t, "a", "c")
assert t == "opciadefghbjklmn"

program = "abcdefghijklmnop"

for line in f:
    instructions = line.split(",")
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

print(program)