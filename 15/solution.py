import numpy as np
import re

BORDER = 2000000

def dist(p0, p1):
    return np.abs(p0[0] - p1[0]) + np.abs(p0[1] - p1[1])

def scan(sensor, beacons):
    min_dist = np.inf
    for beacon in beacons:
        d = dist(beacon, sensor)
        if d < min_dist:
            min_dist = d

    if sensor[1] <= BORDER:
        p = sensor[1] + min_dist
        slice_width = 2 * (p - BORDER) + 1
        r = range(sensor[0] - slice_width // 2, sensor[0] + slice_width // 2 + 1)
        if len(r) > 0:
            return r
    elif sensor[1] >= BORDER:
        p = sensor[1] - min_dist
        slice_width = 2 * (BORDER - p) + 1
        r = range(sensor[0] - slice_width // 2, sensor[0] + slice_width // 2 + 1)
        if len(r) > 0:
            return r

    return None


with open('input') as f:
    lines = [line.strip() for line in f.readlines()]

sensors = []
beacons = []

for line in lines:
    idxs = re.findall(r'-?\d+', line)
    sensors.append((int(idxs[0]), int(idxs[1])))
    beacons.append((int(idxs[2]), int(idxs[3])))

_min = np.inf
_max = -np.inf

ranges = []
for sensor in sensors:
    r = scan(sensor, beacons)
    if r is not None:
        ranges.append(r)
        _min = min(_min, min(r))
        _max = max(_max, max(r) + 1)

impossible_spots = set()
for idx in range(_min, _max):
    for r in ranges:
        if idx in r:
            impossible_spots.add(idx)
            break

for beacon in beacons:
    if beacon[1] == BORDER and beacon[1] in impossible_spots:
        impossible_spots.remove(beacon[1])

print(len(impossible_spots))

