with open('2.txt') as file:
    data = file.read().split('\n\n')


seeds = data[0].split(':')[1].split(' ')[1:]
seeds = [int(x) for x in seeds]

conversions = [group.splitlines() for group in data[1:]]
count = 0

for i in range(0, len(seeds), 2):

    new_seeds = []

    for j in range(seeds[i]):
        if count == 1000:
            print(seeds[i] + j)
            count += 1


lowest_location = float('inf')

# for seed in seeds:
#     current_number = seed
    
#     for group in conversions:
        
#         for line in group[1:]:
#             line_sections = line.split(' ')
            
            
#             dr, sr, rl = map(int, line.split(' '))


#             if sr <= current_number <= sr + rl:
#                 current_number = (dr - sr) + current_number
#                 break
        
#     if current_number < lowest_location:
#         lowest_location = current_number

# print(lowest_location)









                

        














