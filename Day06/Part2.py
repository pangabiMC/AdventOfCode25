import numpy as np
from pathlib import Path

with open(Path(__file__).resolve().parent.joinpath("inputtest")) as file:
    data = [list(line) for line in file] # read the data as character array

# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  

operands = list(filter(lambda item: item != ' ', data[-1])) # last row is the operands, we remove the empty characters
data = np.transpose(data[:-1])

# so now data is like 
# ['1', ' ', ' ']
# ['2', '4', ' ']
# ['3', '5', '6']
# [' ', ' ', ' ']
# etc.

ret = 0
currSum = 0 if operands[0] == '+' else 1
for d in data:
    n = ''.join(d)
    if n.isspace(): # next batch, we will need the next op
        operands = operands[1:]
        ret += currSum
        currSum = 0 if len(operands) > 0 and operands[0] == '+' else 1
    else: # just keep on adding or multiplying this batch
        if operands[0] == '*':
            currSum *= int(n)
        elif operands[0] == '+':
            currSum += int(n)
        else:
            raise Exception('Invalid input operation character')
print(ret)
