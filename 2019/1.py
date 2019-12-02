import re, math

f = open('in/1', 'r')
tot_p1 = 0
tot_p2 = 0
for line in f.read().split("\n"):
    # part 1
    req_fuel = math.floor(int(line)/3) - 2
    tot_p1 += req_fuel
    # part 2
    while req_fuel > 0:
        tot_p2 += req_fuel
        req_fuel = math.floor(req_fuel/3) - 2



print("part1", tot_p1)
print("part2", tot_p2)