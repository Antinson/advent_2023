from collections import defaultdict
import math
import re


with open('2.txt') as file:
    lines = file.read().strip().split('\n')

children = defaultdict(str)

steps = lines[0]
for line in lines[2:]:
    par, left, right = re.search("(...) = \((...), (...)\)", line).groups()
    children[par] = (left, right)

def number_steps(cur):
    count = 0
    while cur[2] != "Z":
        step = steps[count % len(steps)]
        if step == "L":
            cur = children[cur][0]
        else:
            cur = children[cur][1]
        
        count += 1

    return count

cur = [n for n in children if n[2] == "A"]
lens = [number_steps(node) for node in cur]
print(lens)

ans = math.lcm(*lens)
print(ans)