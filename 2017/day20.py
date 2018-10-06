import re
f = open('inputs/day20.txt', 'r')

buffer = []

for line in f:
    particle = {}
    p, v, a  = line.split(">,")
    # probably better way to do this then regex
    r = re.compile("-?\d+")
    particle["p"] = list(map(int, r.findall(p)))
    particle["v"] = list(map(int, r.findall(v)))
    particle["a"] = list(map(int, r.findall(a)))
    particle["dist"] = 0
    buffer.append(particle)

def step(particle):
    particle["v"][0] += particle["a"][0]
    particle["v"][1] += particle["a"][1]
    particle["v"][2] += particle["a"][2]
    particle["p"][0] += particle["v"][0]
    particle["p"][1] += particle["v"][1]
    particle["p"][2] += particle["v"][2]
    particle["dist"] = abs(
        (particle["v"][0] + particle["p"][0] + particle["a"][0]) + 
        (particle["v"][1] + particle["p"][1] + particle["a"][1]) + 
        (particle["v"][2] + particle["p"][2] + particle["a"][2]) 
    )
    return particle

for i in range(0, 100000):
    update()

min_particle = 10000000000
i = 0
index = 0
for particle in buffer:
    if(particle["dist"] < min_particle):
        min_particle = particle["dist"]
        index = i
    i += 1



