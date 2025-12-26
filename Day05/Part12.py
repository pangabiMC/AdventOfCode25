import re
from pathlib import Path
import bisect

with open(Path(__file__).resolve().parent.joinpath("input")) as file:
    data = file.read()

rawRanges = [(int(m[1]), int(m[2])) for m in re.finditer(r"(\d+)-(\d+)", data)]
numbers = list(map(int, filter(lambda v: re.match(r"^(\d+)$", v), data.split('\n'))))

# Sort the ranges at start
rawRanges.sort(key=lambda t: t[0]) 

# Remove overlapping intervals - turns out this is crucial for Part 2
# For Part 1 we need this otherwise the bisect algo doesn't work
distinctRanges = rawRanges[:1]
for begin, end in rawRanges[1:]:
    if begin <= distinctRanges[-1][1]:
        distinctRanges[-1] = (distinctRanges[-1][0], max(end, distinctRanges[-1][1]))
    else:
        distinctRanges.append((begin, end))

# Look at https://docs.python.org/3/library/bisect.html#module-bisect
# bisect returns the index in the sorted list where the item can be inserted and the list remains sorted
# (basically binary search)
# something like: https://stackoverflow.com/a/67405850
#
# Now given sorted and distinct ranges, if a number is NOT in a range, then inserting it into the range start list 
# must give the same index as inserting into the end list
# e.g.
# ranges: [(2, 4), (6, 8)]
# i: 5
#   2, (5), 6 --> bisect: 1
#   4, (5), 8 --> bisect: 1
# but:
# i: 3
#   2, (3), 6 --> bisect: 1
#   (3), 4, 8 --> bisect: 0 
def isGood(i, ranges):
    low = bisect.bisect(ranges, i, key=lambda r: r[0]) # bisect == bisect_right --> if i == r[0] then it inserts to the right
    high = bisect.bisect_left(ranges, i, key=lambda r: r[1]) # bisect_left --> if eq it inserts to the left
    return low != high

# Part 1
result = len([i for i in numbers if isGood(i, distinctRanges)])
print(result)

# Part 2
result = sum([r[1]-r[0]+1 for r in distinctRanges])
print(result)