
with open('2.txt') as file:
    data = file.read().strip().split('\n')

data = [x for x in data if x]

move = {
    'L': 0,
    'R': 1
}

sequence = [x for x in data[0]]

move_data = {}

locations = [[part.strip() for part in x.split('=')] for x in data[1:]]

for loc in locations:
    key, value = loc[0], loc[1]
    move_data[key] = [x.lstrip() for x in value[1:-1].split(',')]

current_key = 'AAA'
count = 0

while True:

    # Gets the L or R data
    current_move = sequence[count % len(sequence)]

    # Gets 0 for L and 1 for R
    move_to_make = move[current_move]

    # Updates the current move to the move location
    current_key = move_data[current_key][move_to_make]

    # We found the end
    if current_key == 'ZZZ':
        count += 1
        break
    
    # We didn't increase count go back to start
    count += 1

print(count)




