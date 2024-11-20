with open('1.txt') as file:
    data = file.readlines()

res = 0

for game in data:
    
    game_id = int(game.split(':')[0][5:])

    game_all = game.split(':')[1].strip()
    game_indv = [x.lstrip(" ") for x in game_all.split(';')]

    count_dict = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for current_game in game_indv:

        current_game_split = [x.lstrip(" ") for x in current_game.split(',')]
        
        for value in current_game_split:
            num, colour = value.split(' ')

            c = count_dict.get(colour, 0)
            count_dict[colour] = c if int(num) < c else int(num)
        

    current_game_power = count_dict['red'] * count_dict['green'] * count_dict['blue']
    print(f"game_id: {game_id} and result: {current_game_power}")
    
    res += current_game_power
        
print(res)