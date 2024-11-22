from collections import deque


with open('2.txt') as file:
    data = file.read().strip().split('\n')


ans = 0

original = []
game_queue = deque()

game_card_cache = {}

def format_card(game_id, game_string):

    if game_id in game_card_cache:
        return game_card_cache[game_id]

    game_id, numbers = game_string.split(":")

    wining_n, user_n = numbers.split('|')

    winning_n = [x for x in wining_n.strip().split(' ') if x]
    user_n = [x for x in user_n.strip().split(' ') if x]

    if game_id not in game_card_cache:
        game_card_cache[game_id] = (winning_n, user_n)

    return winning_n, user_n


for game in data:
    original.append(game)


for game in original:

    game_queue.append(game)

    while game_queue:

        current_game = game_queue.popleft()
        current_game_id = int(current_game.split(':')[0][5:])

        wining_n, user_n = format_card(current_game_id, current_game)

        new_cards = 0

        for n in user_n:
            if n in wining_n:
                new_cards += 1
        
        ans += new_cards
        
        for i in range(0, new_cards):
            game_queue.append(original[current_game_id+i])
 
print(ans + len(original))

    



