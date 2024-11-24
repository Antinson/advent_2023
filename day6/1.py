import re

# Input parsing

with open('2.txt') as file:
    data = file.read().split('\n')

times = [int(x) for x in re.split('\s+', data[0])[1:]]
distances = [int(x) for x in re.split('\s+', data[1])[1:]]

total = 1

# Solving part

for index in range(len(times)):

    time, distance = times[index], distances[index]

    m = 0
    mx = 0

    for i in range(time):
        if (time - i) * i > distance:
            m = i
            print(f"Min is {m}  result is {(time - i) * i} > {distance}")
            break
    
    for i in range(time, 1, -1):
        if (time - i) * i > distance:
            mx = i
            break
    
    print(f"Min {m} \t Max {mx}")
    total *= (mx - m) + 1


print(total)






