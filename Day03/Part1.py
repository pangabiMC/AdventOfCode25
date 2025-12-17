from pathlib import Path

with open(Path(__file__).resolve().parent.joinpath("input")) as file:
    lines = [line.rstrip() for line in file]

ret = 0
for l in lines:
    (i, n) = max(enumerate(l[:-1]), key=lambda x: x[1])
    (j, m) = max(enumerate(l[i+1:]), key=lambda x: x[1])
    ret += int(n+m)

print(ret)