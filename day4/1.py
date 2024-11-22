with open('2.txt') as file:
    data = file.read().strip().split('\n')


ans = 0

for game in data:
    
    game_id, numbers = game.split(":")

    #print(game_id[5:])

    wining_n, user_n = numbers.split('|')
    
    winning_n = [x for x in wining_n.strip().split(' ') if x]
    user_n = [x for x in user_n.strip().split(' ') if x]

    points = 0

    for n in user_n:
        if n in winning_n:
            if points == 0:
                points += 1
            else:
                points *= 2
    
    ans += points

print(ans)