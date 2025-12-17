from pathlib import Path

with open(Path(__file__).resolve().parent.joinpath("input")) as file:
    lines = [line.rstrip() for line in file]

ret = 0

numberOfDigits = 12
for l in lines:
    joltage = ""
    curr = -1
    for r in range(numberOfDigits, 0, -1):
        (i, n) = max(enumerate(l[curr + 1 : None if 1 - r == 0 else 1 - r]), key=lambda x: x[1])
        curr = curr + 1 + i
        joltage = joltage + n
    ret += int(joltage)

print(ret)