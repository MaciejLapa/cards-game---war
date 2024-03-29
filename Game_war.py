colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []

for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)

import random

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

player1 = allCards[:12]
player2 = allCards[12:]


print('-------PLAYER 1--------')
print(player1)

print('-------PLAYER 1--------')
print(player2)

while len(player1) > 0 and len(player2) >0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    stack = []

    if card1["Power"] == card2["Power"]:
        while card1["Power"] == card2["Power"]:
            print("WAR! card1=",card1, "card2 =", card2)
            stack.append(card1)
            stack.append(card2)
            if len(player1) > 2:
                stack.append(player2)
                player1.append(player2)
                player1.clear()
                break
            elif len(player2) > 2:
                stack.append(player1)
                player2.append(player1)
                player2.clear()
                break
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stack.append(card1)
                stack.append(card2)
                card1 = player1.pop(0)
                card2 = player2.pop(0)
        if card1["Power"] > card2["Power"]:
            player1.append(card1)
            player2.append(card1)
            print('Play-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
        else:
            player1.append(card2)
            player1.append(card2)
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player2.append(card1)
        print('Play-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    else:
        player1.append(card2)
        player2.append(card2)
        # print('Play-2 \t %d \t \d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')

if len(player1) > 0:
    print('player 1 won')
else:
    print('Player 2 won')
