count_dict = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}


with open('1.txt') as file:
    data = file.readlines()

res = 0

for game in data:
    
    valid_game = True
    game_id = int(game.split(':')[0][5:])

    game_all = game.split(':')[1].strip()
    game_indv = [x.lstrip(" ") for x in game_all.split(';')]

    for current_game in game_indv:

        current_game_split = [x.lstrip(" ") for x in current_game.split(',')]
        

        for value in current_game_split:
            num, colour = value.split(' ')

            if count_dict[colour.lower()] < int(num):
                valid_game = False
                break
    
    if valid_game:
        res += game_id

print(res)
            
            

 