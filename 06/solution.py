def sweep(s, order):
    s = [[s[i] for i in range(j-order+1, j+1)] for j in range(order - 1, len(s))]
    for i,e in enumerate(s):
        if len(set(e)) == order:
            return i + order

with open('input', 'r') as file:
    inp = file.readline().strip()

    print(sweep(inp, 14))


