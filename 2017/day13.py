with open("inputs/day13.txt") as open_file:
    data = open_file.read().strip().splitlines()

scanners = {}
for line in data:
    scan_depth = int(line.split(':')[0])
    scan_range = int(line.split(':')[1].strip())
    scanners[scan_depth] = scan_range

# part 1
penalty = 0
for scan_depth, scan_range in scanners.items():
    if not scan_depth%(2*(scan_range-1)):
        penalty +=scan_depth*scan_range
print('part 1 penalty:', penalty)

#part2  3913186
lines = [x.rstrip().split(': ') for x in open('inputs/day13.txt','r')]
delay = 1
while delay:
    s = 0
    for line in lines:
        line = [int(x) for x in line]
        sev = (delay + line[0]) % ((line[1] - 1) * 2)
        if not sev:
            s += line[0] * line[1]
            break
    else:
        print(delay)
        break
    delay += 1