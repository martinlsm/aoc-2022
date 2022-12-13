import functools
import numpy as np

def compare(fst, snd):
    if type(fst) is int and type(snd) is int:
        return np.sign(fst - snd)
    if type(fst) is int:
        return compare([fst], snd)
    if type(snd) is int:
        return compare(fst, [snd])

    for x,y in zip(fst, snd):
        cmp = compare(x, y)
        if cmp != 0:
            return cmp

    return np.sign(len(fst) - len(snd))


with open('input') as f:
    lines = [line.strip() for line in f]

pairs = []
i = 0
while i < len(lines):
    line = lines[i]
    if i % 3 == 0:
        # Parse first
        fst = eval(line)
    elif i % 3 == 1:
        snd = eval(line)
        pairs.append((fst, snd))

    i += 1


# Part 1
res = 0
for i,(fst,snd) in enumerate(pairs):
    idx = i + 1
    if compare(fst, snd) == -1:
        res += idx
print(res)


# Part 2
packets = [p for pair in pairs for p in pair] + [[[2]], [[6]]]
res = 1
packets = sorted(packets, key=functools.cmp_to_key(compare))
for i,packet in enumerate(packets):
    idx = i + 1
    if packet == [[2]] or packet == [[6]]:
        res *= idx
print(res)
