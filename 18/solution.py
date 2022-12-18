import re

def adjacent(p):
    x,y,z = p
    return [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    ]

with open('input') as f:
    lines = [line.strip() for line in f]
    cubes = set([tuple(int(n) for n in re.findall(r'\d+', line)) for line in lines])

# Part 1
surface_area = 0
for (x,y,z) in cubes:
    surface_area += 1 if (x + 1, y, z) not in cubes else 0
    surface_area += 1 if (x - 1, y, z) not in cubes else 0
    surface_area += 1 if (x, y + 1, z) not in cubes else 0
    surface_area += 1 if (x, y - 1, z) not in cubes else 0
    surface_area += 1 if (x, y, z + 1) not in cubes else 0
    surface_area += 1 if (x, y, z - 1) not in cubes else 0

print(surface_area)

# Part 2
lowest_x  = min((x for (x,_,_) in cubes)) - 1
highest_x = max((x for (x,_,_) in cubes)) + 1
lowest_y  = min((y for (_,y,_) in cubes)) - 1
highest_y = max((y for (_,y,_) in cubes)) + 1
lowest_z  = min((z for (_,_,z) in cubes)) - 1
highest_z = max((z for (_,_,z) in cubes)) + 1

start = (lowest_x, lowest_y, lowest_z)
visited = set([start])
flood_fill_stack = [start]
surface_area = 0

while len(flood_fill_stack) > 0:
    cube = flood_fill_stack.pop()

    for adj in adjacent(cube):
        if adj not in cubes and adj not in visited \
                and adj[0] in range(lowest_x, highest_x + 1) \
                and adj[1] in range(lowest_y, highest_y + 1) \
                and adj[2] in range(lowest_z, highest_z + 1):
            visited.add(adj)
            flood_fill_stack.append(adj)
        elif adj in cubes:
            surface_area += 1

print(surface_area)
