filename = "Day01/input"
lines = []
with open(filename) as file:
    lines = [line.rstrip() for line in file]

# part 1
dial = 50
pwd = 0
for l in lines:
    dir = l[0]
    step = int(l[1:])
    dial = (dial + (-1 if dir == 'L' else +1) * step + 100) % 100
    if dial == 0:
        pwd += 1

print(pwd)

# part 2
def Turn(dial, turn):
    pwd = 0
    step = (-1 if turn[0] == 'L' else 1) * int(turn[1:])
    wasZero = dial == 0
    dial += step
    if dial > 99:
        pwd = dial // 100
    elif dial < 0 and not wasZero:
        pwd = (dial - 100) // -100
    elif dial < 0:
        pwd = dial // -100
    elif dial == 0:
        pwd = 1
    
    dial = (dial % 100 + 100) % 100
    
    if dial < 0 or dial >= 100:
        raise RuntimeError("dial is out of bounds: " + dial)
    return [pwd, dial]

d = 50
p = 0
for l in lines:
    r = Turn(d, l)
    d = r[1]
    p += r[0]
print(p)


# assert Turn(50, "L20")[1] == 30
# assert Turn(50, "R20")[1] == 70
# assert Turn(50, "L50")[1] == 0
# assert Turn(50, "R50")[1] == 0
# assert Turn(50, "L270")[1] == 80
# assert Turn(50, "R270")[1] == 20
# assert Turn(0, "L20")[1] == 80
# assert Turn(0, "R20")[1] == 20
# assert Turn(0, "L50")[1] == 50
# assert Turn(0, "R50")[1] == 50
# assert Turn(0, "L270")[1] == 30
# assert Turn(0, "R270")[1] == 70


# assert Turn(50, "L20") == [0, 30]
# assert Turn(50, "R20") == [0, 70]
# assert Turn(50, "L50") == [1, 0]
# assert Turn(50, "R50") == [1, 0]
# assert Turn(50, "L70") == [1, 80]
# assert Turn(50, "R70") == [1, 20]
# assert Turn(50, "L120") == [1, 30]
# assert Turn(50, "R120") == [1, 70]
# assert Turn(50, "L170") == [2, 80]
# assert Turn(50, "R170") == [2, 20]
# assert Turn(50, "L570") == [6, 80]
# assert Turn(50, "R570") == [6, 20]
# assert Turn(50, "L150") == [2, 0]
# assert Turn(50, "R150") == [2, 0]

# assert Turn(0, "L20") == [0, 80]
# assert Turn(0, "R20") == [0, 20]
# assert Turn(0, "L100") == [1, 0]
# assert Turn(0, "R100") == [1, 0]
# assert Turn(0, "L170") == [1, 30]
# assert Turn(0, "R170") == [1, 70]
# assert Turn(0, "L200") == [2, 0]
# assert Turn(0, "R200") == [2, 0]
# assert Turn(0, "L270") == [2, 30]
# assert Turn(0, "R270") == [2, 70]
