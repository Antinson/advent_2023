import re

# Input parsing

with open('2.txt') as file:
    data = file.read().split('\n')

times = [int(x) for x in re.split('\s+', data[0])[1:]]
distances = [int(x) for x in re.split('\s+', data[1])[1:]]


new_times = int(''.join(map(str, times)))
new_distances = int(''.join(map(str, distances)))



time, distance = new_times, new_distances

m = 0
mx = 0

for i in range(time):
    if (time - i) * i > distance:
        m = i
        break

for i in range(time, 1, -1):
    if (time - i) * i > distance:
        mx = i
        break

print(mx - m + 1)







