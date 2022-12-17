import numpy as np
import re

class Sensor:
    def __init__(self, pos):
        self.pos = pos

    def set_scan_dist(self, dist):
        self.dist = dist

    def go_to_right_edge(self, p):
        (px, py) = p
        (sx, sy) = self.pos

        top_corner = sy - self.dist
        if top_corner <= py <= sy:
            slice_width = 2 * (py - top_corner) + 1
            if px in range(sx - slice_width // 2, sx + slice_width // 2 + 1):
                return (sx + slice_width // 2 + 1, py)

        bottom_corner = sy + self.dist
        if sy <= py <= bottom_corner:
            slice_width = 2 * (bottom_corner - py) + 1
            if px in range(sx - slice_width // 2, sx + slice_width // 2 + 1):
                return (sx + slice_width // 2 + 1, py)


        return p


def manhattan_dist(p0, p1):
    return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])

def scan(sensor_pos, beacons):
    min_dist = np.inf
    for beacon in beacons:
        d = manhattan_dist(beacon, sensor_pos)
        if d < min_dist:
            min_dist = d

    return min_dist


with open('input') as f:
    lines = [line.strip() for line in f.readlines()]

sensors = []
beacons = []

for line in lines:
    idxs = re.findall(r'-?\d+', line)
    sensors.append(Sensor((int(idxs[0]), int(idxs[1]))))
    beacons.append((int(idxs[2]), int(idxs[3])))

for sensor in sensors:
    dist = scan(sensor.pos, beacons)
    sensor.set_scan_dist(dist)

max_dim = 4000000
x = 0
y = 0
while True:
    x_next = x
    for sensor in sensors:
        (x_next, _) = sensor.go_to_right_edge((x_next, y))

    if x_next == x:
        tuning_freq = 4000000 * x + y
        print(tuning_freq)
        break

    if x_next >= max_dim:
        x = 0
        y += 1
        if y >= max_dim:
            break
    else:
        x = x_next





