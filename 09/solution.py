def above(p0, p1):
    return p0[1] > p1[1]

def below(p0, p1):
    return p0[1] < p1[1]

def left_of(p0, p1):
    return p0[0] < p1[0]

def right_of(p0, p1):
    return p0[0] > p1[0]

def same_x(p0, p1):
    return p0[0] == p1[0]

def same_y(p0, p1):
    return p0[1] == p1[1]

class Rope:
    def __init__(self):
        self.head = (0,0)
        self.tail = (0,0)
        self.tail_visited = set([self.tail])

    def R(self):
        if self.tail[0] < self.head[0]:
            self.tail = self.head
            self.tail_visited.add(self.tail)
        self.head = (self.head[0] + 1, self.head[1])

    def L(self):
        if self.tail[0] > self.head[0]:
            self.tail = self.head
            self.tail_visited.add(self.tail)
        self.head = (self.head[0] - 1, self.head[1])

    def U(self):
        if self.tail[1] < self.head[1]:
            self.tail = self.head
            self.tail_visited.add(self.tail)
        self.head = (self.head[0], self.head[1] + 1)

    def D(self):
        if self.tail[1] > self.head[1]:
            self.tail = self.head
            self.tail_visited.add(self.tail)
        self.head = (self.head[0], self.head[1] - 1)

class LongRope:
    def __init__(self, length):
        self.head = (0,0)
        self.tail = LongRope(length - 1) if length > 1 else None
        self.visited = set([self.head])

    def RU(self):
        h = self.head
        if self.tail is not None:
            t = self.tail.head
            if not right_of(t, h) and not above(t, h) and t != h:
                self.tail.RU()
            elif above(t, h) and left_of(t, h):
                self.tail.R()
            elif below(t, h) and right_of(t, h):
                self.tail.U()
        self.head = (h[0] + 1, h[1] + 1)
        self.visited.add(self.head)

    def LU(self):
        h = self.head
        if self.tail is not None:
            t = self.tail.head
            if not left_of(t, h) and not above(t, h) and t != h:
                self.tail.LU()
            elif right_of(t, h) and above(t, h):
                self.tail.L()
            elif left_of(t, h) and below(t, h):
                self.tail.U()
        self.head = (h[0] - 1, h[1] + 1)
        self.visited.add(self.head)

    def RD(self):
        h = self.head
        if self.tail is not None:
            t = self.tail.head
            if not right_of(t, h) and not below(t, h) and t != h:
                self.tail.RD()
            elif right_of(t, h) and above(t, h):
                self.tail.D()
            elif left_of(t, h) and below(t, h):
                self.tail.R()
        self.head = (h[0] + 1, h[1] - 1)
        self.visited.add(self.head)

    def LD(self):
        h = self.head
        if self.tail is not None:
            t = self.tail.head
            if not left_of(t, h) and not below(t, h) and t != h:
                self.tail.LD()
            elif left_of(t, h) and above(t, h):
                self.tail.D()
            elif right_of(t, h) and below(t, h):
                self.tail.L()
        self.head = (h[0] - 1, h[1] - 1)
        self.visited.add(self.head)

    def R(self):
        h = self.head
        if self.tail is not None:
            t = self.tail.head
            if left_of(t, h):
                if above(t, h):
                    self.tail.RD()
                elif below(t, h):
                    self.tail.RU()
                else:
                    self.tail.R()
        self.head = (h[0] + 1, h[1])
        self.visited.add(self.head)

    def D(self):
        h = self.head
        if self.tail is not None:
            t = self.tail.head
            if above(t, h):
                if left_of(t, h):
                    self.tail.RD()
                elif right_of(t, h):
                    self.tail.LD()
                else:
                    self.tail.D()
        self.head = (h[0], h[1] - 1)
        self.visited.add(self.head)

    def L(self):
        h = self.head
        if self.tail is not None:
            t = self.tail.head
            if right_of(t, h):
                if above(t, h):
                    self.tail.LD()
                elif below(t, h):
                    self.tail.LU()
                else:
                    self.tail.L()
        self.head = (h[0] - 1, h[1])
        self.visited.add(self.head)

    def U(self):
        h = self.head
        if self.tail is not None:
            t = self.tail.head
            if below(t, h):
                if left_of(t, h):
                    self.tail.RU()
                elif right_of(t, h):
                    self.tail.LU()
                else:
                    self.tail.U()
        self.head = (h[0], h[1] + 1)
        self.visited.add(self.head)

    def get_tail_tip_visited(self):
        if self.tail is None:
            return self.visited
        return self.tail.get_tail_tip_visited()

    def print(self, x0, y0, x1, y1):
        grid = [['.' for _ in range(x1 - x0)] for _ in range(y1 - y0)]
        self._print_helper(grid, 0, x0, y0)
        print('\n'.join(reversed([''.join(row) for row in grid])))

    def _print_helper(self, grid, n, x0, y0):
        (x,y) = self.head
        if n == 0:
            grid[y - y0][x - x0] = 'H'
        elif grid[y - y0][x - x0] == '.':
            grid[y - y0][x - x0] = str(n)

        if self.tail is not None:
            self.tail._print_helper(grid, n + 1, x0, y0)


with open('input') as f:
    lines = [x.strip().split() for x in f.readlines()]
    cmds = [(x[0], int(x[1])) for x in lines]

# Part 1
rope = Rope()
for dir,steps in cmds:
    cmd = getattr(rope, dir)
    for _ in range(steps):
        cmd()
print(len(rope.tail_visited))

# Part 2
long_rope = LongRope(10)
for dir,steps in cmds:
    cmd = getattr(long_rope, dir)
    for _ in range(steps):
        cmd()
print(len(long_rope.get_tail_tip_visited()))
