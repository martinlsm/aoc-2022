import numpy as np
import matplotlib.pyplot as plt

def can_go_left(pos, shape, chamber):
    w,h = shape.shape
    x,y = pos
    for yy in range(h):
        for xx in range(w):
            if shape[xx, yy] != 0:
                if chamber[x + xx - 1, y + yy] == 0:
                    break
                else:
                    return False
    return True

def can_go_right(pos, shape, chamber):
    w,h = shape.shape
    x,y = pos
    for yy in range(h):
        for xx in range(w - 1, -1, -1):
            if shape[xx, yy] != 0:
                if chamber[x + xx + 1, y + yy] == 0:
                    break
                else:
                    return False
    return True

def can_fall(pos, shape, chamber):
    w,h = shape.shape
    x,y = pos
    for xx in range(w):
        for yy in range(h):
            if shape[xx, yy] != 0:
                if chamber[x + xx, y + yy - 1] == 0:
                    break
                else:
                    return False
    return True



with open('input', 'r') as f:
    lines = [line.strip() for line in f]
jet_pattern = lines[0]


chamber_height = 1000000
chamber = np.zeros(shape=(9, chamber_height))
chamber[:,0]  = 1
chamber[0,:]  = 1
chamber[-1,:] = 1

shapes = [
    np.rot90(np.array([[1,1,1,1]], dtype=np.uint8), axes=(1,0)),
    np.rot90(np.array([[0,1,0],
                       [1,1,1],
                       [0,1,0]], dtype=np.uint8), axes=(1,0)),
    np.rot90(np.array([[0,0,1],
                       [0,0,1],
                       [1,1,1]], dtype=np.uint8), axes=(1,0)),
    np.rot90(np.array([[1],
                       [1],
                       [1],
                       [1]], dtype=np.uint8), axes=(1,0)),
    np.rot90(np.array([[1,1],
                       [1,1]], dtype=np.uint8), axes=(1,0)),
]

shape_heights = [1, 3, 3, 4, 2]

jet_pattern_idx = 0
highest_point = 0
num_rocks = 20000

cycle_dict = {}
cycle_started = None

# test
#cycle_start = 43
#cycle_start_height = 70
#cycle_len = 35
#cycle_height_gain = 53

# real case
cycle_start = 1738
cycle_start_height = 2671
cycle_len = 1730
cycle_height_gain = 2644

iter_per_repetition = len(jet_pattern) * len(shapes)
print(iter_per_repetition)

for shape_idx in range(num_rocks):
    shape = shapes[shape_idx % len(shapes)]
    x,y = 3, highest_point + 4

    while True:
        if shape_idx % len(shapes) == 3 and jet_pattern_idx % len(jet_pattern) == 0:
            if cycle_started is None:
                cycle_started = False
            elif cycle_started == False:
                cycle_started = True
            print(shape_idx, highest_point)
            xs.append(shape_idx)
            ys.append(highest_point)

        # apply push
        direction = jet_pattern[jet_pattern_idx % len(jet_pattern)]
        match direction:
            case '<':
                if can_go_left((x,y), shape, chamber):
                    #print('go left')
                    x -= 1
                else:
                    pass
                    #print('can\'t go left')
            case '>':
                if can_go_right((x,y), shape, chamber):
                    #print('go right')
                    x += 1
                else:
                    pass
                    #print('can\'t go right')
        jet_pattern_idx += 1

        # apply fall
        if can_fall((x,y), shape, chamber):
            #print('fall down')
            y -= 1
        else:
            #print('can\'t fall down')
            chamber[x:x+shape.shape[0], y:y+shape.shape[1]] = \
                    np.logical_or(chamber[x:x+shape.shape[0], y:y+shape.shape[1]],
                                  shape).astype(np.uint8)

            highest_point = max(highest_point, y + shape_heights[shape_idx % len(shapes)] - 1)
            break

    if cycle_started is not None and cycle_started:
        cycle_dict[(shape_idx - cycle_start) % cycle_len] = (highest_point - cycle_start_height - 1) % cycle_height_gain


print(chamber)
print(highest_point)

rocks = 1000000000000
height = 0

rocks -= cycle_start
height += cycle_start_height

num_cycles = rocks // cycle_len
height += num_cycles * cycle_height_gain

print(height)

rocks = rocks % cycle_len
height += cycle_dict[rocks]

print(height)
