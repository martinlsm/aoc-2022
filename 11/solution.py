from copy import deepcopy
import numpy as np

class MonkeyFunc:
    def __init__(self, op, fst, snd):
        self.op = op
        self.fst = fst
        self.snd = snd

    def __call__(self, item):
        arg1 = item if self.fst == 'old' else int(self.fst)
        arg2 = item if self.snd == 'old' else int(self.snd)
        match self.op:
            case '+':
                f = lambda x,y: x + y
            case '*':
                f = lambda x,y: x * y
        return f(arg1, arg2)

def prog(part):
    monkeys = []

    # Parse monkeys
    with open('input') as f:
        for line in f:
            line = line[:-1]
            if line.startswith('Monkey'):
                n = int(line[7])
            elif line.startswith('  Starting items'):
                line = line[18:]
                items = [int(x) for x in line.split(', ')]
            elif line.startswith('  Operation:'):
                line = line[19:]
                cmd = line.split(' ')
                func = MonkeyFunc(cmd[1], cmd[0], cmd[2])
            elif line.startswith('  Test: '):
                test_mod = int(line[21:])
            elif line.startswith('    If true:'):
                true_monkey = int(line[-1])
            elif line.startswith('    If false:'):
                false_monkey = int(line[-1])
                monkeys.append([n, items, func, test_mod, true_monkey, false_monkey])

    reduction = np.prod([m[3] for m in monkeys])
    inspections = [0 for _ in monkeys]
    for i in range(20 if part == 1 else 10000):
        for m in monkeys:
            inspections[m[0]] += len(m[1])
            for item in m[1]:
                x = m[2](item)
                if part == 1:
                    x = x // 3
                x = x % reduction
                if x % m[3] == 0:
                    monkeys[m[4]][1].append(x)
                else:
                    monkeys[m[5]][1].append(x)
            m[1] = []

    print(np.prod(sorted(inspections)[-2:]))

prog(1)
prog(2)
