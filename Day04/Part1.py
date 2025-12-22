from pathlib import Path
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

with open(Path(__file__).resolve().parent.joinpath("inputtest")) as file:
    map = np.array([list(line.strip()) for line in file])

# pad the map with . on each sides
map = np.pad(map, 1, mode='constant', constant_values='.')

# now just simply count all windows
ret = 0
windows = sliding_window_view(map, window_shape=(3, 3))
windows = windows.reshape(-1, windows.shape[-2], windows.shape[-1])
for window in windows:
    if window[1][1] == '@' and np.count_nonzero(window == '@') < 5:
       ret += 1
print(ret)
