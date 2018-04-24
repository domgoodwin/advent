# Generator A starts with 703
# Generator B starts with 516

# The generators both work on the same principle. To create its next value, 
# a generator will take the previous value it produced, multiply it by a factor 
# (generator A uses 16807; generator B uses 48271), and then keep the remainder 
# of dividing that resulting product by 2147483647. That final remainder is the value it produces next.

# To calculate each generator's first value, it instead uses a specific starting value as its "previous value" (as listed in your puzzle input).

def convertAndCompare(a, b):
        bin_a = "{0:b}".format(a)
        bin_b = "{0:b}".format(b)
        return bin_a[-16:] == bin_b[-16:]

gen_a = 703
gen_b = 516
loop = 40000000
matches = 0

for i in range(0, loop):
    gen_a = (gen_a * 16807) % 2147483647
    gen_b = gen_b * 48271 % 2147483647
    if(convertAndCompare(gen_a, gen_b)):
        matches += 1

print(matches)


