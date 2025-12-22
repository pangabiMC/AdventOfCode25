from pathlib import Path
import numpy as np

with open(Path(__file__).resolve().parent.joinpath("input")) as file:
    m = np.array([list(line.strip()) for line in file])

RemovableThreshold = 4

# we replace the original map with a map of number of neighbours
def CountNeighbours(m: any, x: int, y: int) -> int:
    if m[x][y] == '.':
        return -1
    if m[x][y] == '@':
        return (m[x-1:x+2, y-1:y+2] == '@').sum() - 1

# then on each iteration we decrease the numbers in that map
def TryRemoveCrate(m: any, x: int, y: int) -> bool:
    if m[x][y] == -1 or m[x][y] >= RemovableThreshold:
        return False
    sub = m[x-1:x+2, y-1:y+2]
    sub[sub > 0] -= 1
    m[x][y] = -1
    return True

# pad the map with . on each sides to avoid dealing with out of bounds
m = np.pad(m, 1, mode='constant', constant_values='.')

# create the neighbours count map
mapNum = np.zeros(m.shape)
for iy, ix in np.ndindex(m.shape):
    mapNum[ix][iy] = CountNeighbours(m, ix, iy)

# keep on removing while we can
ret = 0
while True:
    thisRun = sum(TryRemoveCrate(mapNum, i, j) for i, j in np.ndindex(mapNum.shape))
    ret += thisRun
    if thisRun == 0:
        break
print(ret)