RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

with open('1.txt') as file:
    for line in file:
        line = line.strip()
        new_data = line.split(':')
        game_line = [x.strip().split(';') for x in new_data[1:]]
        for game in game_line:
            for x in game:  
                print(x.split(',') + '\n')



# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Split on the : & get the number after so could do [5 till the :