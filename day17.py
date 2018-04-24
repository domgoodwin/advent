step = 377
pos = 0
vals = [0]

for i in range(1,2018):
    pos = ((pos + step) % len(vals)) + 1
    vals.insert(pos, i)

print(vals[vals.index(2017) + 1])

#part 2
# step = 377
pos = 0
len_vals = 1

#had to change this so it didn't take 4hrs to run
for i in range(50000000):
    val = i+1
    new = (pos + step) % len_vals
    new += 1
    if new == 1:
        part2 = val
    pos = new
    len_vals += 1
print(part2)
