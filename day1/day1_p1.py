sum_total = 0

for x in open('1.txt'):
    digits = [ch for ch in x if ch.isdigit()]
    sum_total += int(digits[0] + digits[-1])

print(sum_total)

    
