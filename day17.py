step = 377
pos = 0
vals = [0]

for i in range(1,2018):
    pos = ((pos + step) % len(vals)) + 1
    vals.insert(pos, i)
    print(pos, i)

print(vals[vals.index(2017) + 1])
