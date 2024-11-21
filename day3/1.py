with open('2.txt') as file:
    data = file.read().strip().split('\n')


line_length = len(data[0])
column_length = len(data)
ans = 0


def is_symbol(col, loc):
    if col < 0 or col >= column_length or loc < 0 or loc >= line_length:
        return False
    
    return data[col][loc] != '.' and not data[col][loc].isdigit()

for col, line in enumerate(data):

    current_pos = 0
    start = 0

    while current_pos < line_length:
        
        start = current_pos
        num = ""
        while current_pos < line_length and line[current_pos].isdigit():
            num += line[current_pos]
            current_pos += 1
        
        if num == "":
            current_pos += 1
            continue
        
        num = int(num)

        if is_symbol(col, start-1) or is_symbol(col, current_pos):
            ans += num
            current_pos += 1
            continue

        for k in range(start-1, current_pos+1):
            if is_symbol(col-1, k) or is_symbol(col+1, k):
                ans += num
                break

print(ans)

        






