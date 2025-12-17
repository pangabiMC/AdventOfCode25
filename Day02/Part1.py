import re
from pathlib import Path
with open(Path(__file__).resolve().parent.joinpath("inputtest")) as file:
    data = file.read()
    
rangeregex = r"(\d+)-(\d+)"
ranges = [(int(m[1]), int(m[2])) for m in re.finditer(rangeregex, data)]

def evenLen(n: int) -> bool:
    return len(str(n)) % 2 == 0

def roundUp(n: int) -> int:
    return 10 ** (len(str(n)))

def roundDown(n: int) -> int:
    return 10 ** (len(str(n)) - 1) - 1

def splitNumber(n: int) -> int:
    return int(str(n)[:len(str(n))//2])

def doubleNumber(n: int) -> int:
    return int(str(n) + str(n))

def sanitiseRanges(r: list) -> list:
    sanList = []
    for i, s in enumerate(ranges):
        if abs(len(str(s[0])) - len(str(s[1]))) > 1:
            raise Exception("Input range with wide for this algorithm") 
        if not evenLen(s[0]) and not evenLen(s[1]):
            continue
        if not evenLen(s[0]):
            sanList.append((roundUp(s[0]), s[1]))
        elif not evenLen(s[1]):
            sanList.append((s[0], roundDown(s[1])))
        else:
            sanList.append(s)
    return sanList

ret = 0
ranges = sanitiseRanges(ranges)

for r in ranges:
    id = splitNumber(r[0]) - 1
    while True:
        id += 1
        dbl = doubleNumber(id)
        if r[0] <= dbl <= r[1]:
            ret += dbl
        if dbl > r[1]:
            break

print(ret)
    