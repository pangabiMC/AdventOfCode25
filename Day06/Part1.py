import numpy as np
import math
from pathlib import Path

with open(Path(__file__).resolve().parent.joinpath("inputtest")) as file:
    data = np.array([list(line.split()) for line in file])

# this is easy with numpy, we just transpose the number matrix and sum or prod up each row
data = np.transpose(data) 
ret = 0
for line in data:
    if line[-1] == '*':
        ret += math.prod(map(int, line[:-1]))
    elif line[-1] == '+':
        ret += sum(map(int, line[:-1]))
    else:
        raise Exception('Invalid input operation character')
print(ret)
