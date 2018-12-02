# todo
f = open('inputs/day7.txt', 'r')
# find root node in tree
part1 = ''

def find(discs, name):
    for disc in discs:
        if(disc.name == name):
            return disc

class Disc:
    def __init__(self, name):
        self.name = name
        self.towers = []
        self.realTowers = []
        self.weight = 0
        self.towersWeight = 0
        self.parents = []
    def addSubTower(self, towers):
        self.towers = [x.strip() for x in towers.split(',')]
    def addWeight(self, weight):
        self.weight = weight
        self.towersWeight += weight
    def addParent(self, parent):
        self.parents.append(parent)
    def addSubTowers2(self, discs):
        for tower in self.towers:
            self.realTowers.append(find(discs, tower))
    def calculateWeight(self):
        for tower in self.realTowers:
            if(tower is None): break;
            self.towersWeight += tower.calculateWeight()
        return self.towersWeight
    def check(self):
        checkWeight = 0
        for tower in self.realTowers:
            checkWeight += tower.weight
        print(str(checkWeight) + " // " + str(self.weight))
        return self.towersWeight
    def print(self):
        print(self.name + " // " + str(self.weight) + " // " + str(self.towers) + " // " + str(self.parents) + " // " + str(self.towersWeight))




discs = []
for line in f:
    #do something
    sp = line.split("->")
    subs = ''
    if(len(sp) > 1): 
        subs = sp[1].strip()
    endOfN = line.find("(")
    name = line[0: endOfN].strip()
    weight = int(line[endOfN + 1: line.find(")")])
    disc = Disc(name)
    disc.addSubTower(subs)
    disc.addWeight(weight)
    discs.append(disc)

for disc in discs:
    for tower in disc.towers:
        d = next((x for x in discs if x.name == tower), None)
        if(d is None):
            part1 = disc
        else:
            d.addParent(disc.name)

for disc in discs:
    ##disc.print()
    if(len(disc.parents) == 0): part1 = disc.name
    disc.addSubTowers2(discs)

print(part1)

for tower in find(discs, "ptshtrn").towers:
    t = find(discs, tower)
    t.calculateWeight()
    t.print()


