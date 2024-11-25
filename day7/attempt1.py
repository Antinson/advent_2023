
# Parse

with open('1.txt') as file:
    data = file.readlines()

data = [x.split() for x in data]


cards = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10
}


# Process
types = [[] for _ in range(7)] 

for card in data:

    card_values = card[0]
    c_count = [[] for _ in range(15)]
    temp_types = 0
    
    for n in card_values:
        if n in cards:
            n = cards[n]
        
        c_count[int(n)].append(int(n))

        if len(c_count[int(n)]) == 5:
            temp_types = 6
        elif len(c_count[int(n)]) == 4:
            temp_types = 5
    

    len_3 = 0
    len_2 = 0
        
    if temp_types < 4:

        
        for location in c_count:
            
            if len(location) == 3:
                len_3 = 1
            
            if len(location) == 2:
                len_2 += 1
        
        if len_3 == 1 and len_2 == 1:
            temp_types = 4
        elif len_3 == 1 and len_2 == 0:
            temp_types = 3
        elif len_2 == 2:
            temp_types = 2
        elif len_2 == 1:
            temp_types = 1
        else:
            temp_types = 0
    
    types[temp_types].append(card)
        

    
for i in range(len(types)):
    print(f"Rank: {i} \t Cards: {types[i]}")

    

        



                


    






