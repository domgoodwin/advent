f = open('inputs/day22.txt', 'r')

class Virus:
    def __init__(self, dir, pos):
        self.dir = dir # North
        self.pos = pos
    def turn(self, right):
        if(right):
            self.dir = (self.dir + 1) % 4
        else:
            self.dir = (self.dir - 1) % 4
    def action(self, cur_node):
        #return "#" if cur_node == "." else "."
        if(cur_node == "."):
            return "w"
        elif(cur_node == "w"):
            return "#"
        elif(cur_node == "i"):
            return "f"
        else:
            return "."
    def move(self, amount):
        if(self.dir == 0):
            self.pos[1] = self.pos[1] - amount
        elif(self.dir == 1):
            self.pos[0] = self.pos[0] + amount
        elif(self.dir == 2):
            self.pos[1] = self.pos[1] + amount
        elif(self.dir == 3):
            self.pos[0] = self.pos[0] - amount

class Grid:
    def __init__(self, f):
        self.matrix = []
        self.create(f)
        mid = int((len(self.matrix) - 1) / 2)
        self.v = Virus(0, [mid, mid])
        self.i_count = 0
    def create(self, f):
        for i, line in enumerate(f):
            self.matrix.append([]) 
            for ch in line.strip():
                self.matrix[i].append(ch)
    def burst(self):
        cur_node = self.matrix[self.v.pos[1]][self.v.pos[0]]
        self.v.turn(cur_node == "#")
        n_cur = self.v.action(cur_node)
        if(n_cur == "#"): self.i_count += 1
        self.matrix[self.v.pos[1]][self.v.pos[0]] = n_cur
        self.move_v(1)
    def move_v(self, amount):
        if(self.v.dir == 0):
            self.v.pos[1] = self.v.pos[1] - amount
            if(self.v.pos[1] < 0):
                self.addRow(0)
                self.v.pos[1] = 0
        elif(self.v.dir == 1):
            self.v.pos[0] = self.v.pos[0] + amount
            if(self.v.pos[0] >= len(self.matrix[0])):
                self.addCol(len(self.matrix[0]))
        elif(self.v.dir == 2):
            self.v.pos[1] = self.v.pos[1] + amount
            if(self.v.pos[1] >= len(self.matrix) - 1):
                self.addRow(len(self.matrix))
        elif(self.v.dir == 3):
            self.v.pos[0] = self.v.pos[0] - amount
            if(self.v.pos[0] < 0):
                self.addCol(0)
                self.v.pos[0] = 0
    def addRow(self, pos):
        self.matrix.insert(pos, ['.' for i in self.matrix[0]])
    def addCol(self, pos):
        n_matrix = []
        for row in self.matrix:
            row.insert(pos, '.')
            n_matrix.append(row)
        self.matrix = n_matrix
    def print(self):
        full = ""
        for y, row in enumerate(self.matrix):
            for x, ch in enumerate(row):
                if(y == self.v.pos[1] and x == self.v.pos[0]):
                    full += '[' + ch + ']'
                else:
                    full += ' ' + ch + ' '
            full += '\n'
        print(full)

g = Grid(f)
i = 0
while(i < 10000000):
    g.burst()
    i += 1

print(g.i_count) 
g.print()