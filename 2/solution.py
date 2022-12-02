d = {'A': 'rock', 'B': 'paper', 'C': 'scissors',
     'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

def points(a, b):
    res = 0
    if a == 'rock':
        res += 1
        if b == 'scissors':
            res += 6
        elif b == 'rock':
            res += 3
    elif a == 'paper':
        res += 2
        if b == 'rock':
            res += 6
        elif b == 'paper':
            res += 3
    elif a == 'scissors':
        res += 3
        if b == 'paper':
            res += 6
        elif b == 'scissors':
            res += 3

    return res

def points2(a, b):
    res = 0
    if a == 'X':
        res += 0
    elif a == 'Y':
        res += 3
    elif a == 'Z':
        res += 6

    # you play rock
    if b == 'scissors' and a == 'Z' or b == 'rock' and a == 'Y' or b == 'paper' and a == 'X':
        res += 1
    # you play paper
    if b == 'rock' and a == 'Z' or b == 'paper' and a == 'Y' or b == 'scissors' and a == 'X':
        res += 2
    # you play scissors
    if b == 'paper' and a == 'Z' or b == 'scissors' and a == 'Y' or b == 'rock' and a == 'X':
        res += 3

    return res


#p = 0
#with open('input', 'r') as inp:
#    for line in inp.readlines():
#        (a, b) = (d[x] for x in line.strip().split(' '))
#        print((a,b))
#        p += points(b, a)
#
#print(p)

p = 0
with open('input', 'r') as inp:
    for line in inp.readlines():
        (a, b) = line.strip().split(' ')
        a = d[a]
        p += points2(b, a)

print(p)
