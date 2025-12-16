import re

filename = "Day02/inputtest"
with open(filename) as file:
    data = file.read()
rangeregex = r"(\d+)-(\d+)"
ranges = [(m[1], m[2]) for m in re.finditer(rangeregex, data)]
print(ranges)
for i, s in enumerate(ranges):
    if len(str(s[0])) % 2 != 0:
        print(s[0])
        #ranges[i] = [111, s[1]]

print(ranges)