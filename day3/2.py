with open('2.txt') as file:
    data = file.read().strip().split('\n')


line_length = len(data[0])
column_length = len(data)
ans = 0

goods = [[[] for _ in range(line_length)] for _ in range(column_length)]

def is_symbol(col, loc, num):
    if col < 0 or col >= column_length or loc < 0 or loc >= line_length:
        return False
    
    if data[col][loc] == "*":
        return goods[col][loc].append(num)
    
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

        is_symbol(col, start-1, num) or is_symbol(col, current_pos, num)


        for k in range(start-1, current_pos+1):
            is_symbol(col-1, k, num) or is_symbol(col+1, k, num)

for i in range(line_length):
    for j in range(column_length):
        nums = goods[i][j]
        if data[i][j] == "*" and len(nums) == 2:
            ans += nums[0] * nums[1]
        

print(ans)

        






