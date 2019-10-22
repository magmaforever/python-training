# Black Jack game!

import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

random.shuffle(deck)

print(
    "                       **********************************************************                                    "
)
print(
    "                               Welcome to the game Casino - BLACK JACK !                                             "
)
print(
    "                       **********************************************************                                    "
)

d_cards = []  # 初始化庄家的牌
p_cards = []  # 初始化玩家的牌

while len(d_cards) != 2:
    random.shuffle(deck)
    d_cards.append(deck.pop())
    if len(d_cards) == 2:
        print('The cards dealer has are X ', d_cards[1])

# 显示玩家的牌
while len(p_cards) != 2:
    random.shuffle(deck)
    p_cards.append(deck.pop())
    if len(p_cards) == 2:
        print('The total of player is ', sum(p_cards))
        print('The cards Player has are ', p_cards)

if sum(p_cards) > 21:
    print(
        'You are BUSTED !\n ****************Dealer Wins !!****************\n')
    exit()

if sum(d_cards) > 21:
    print('Dealer is BUSTED !\n ****************You Win !!****************')
    exit()

if sum(d_cards) == 21:
    print('****************Dealer is the Winner !!****************')
    exit()

if sum(d_cards) == 21 and sum(p_cards) == 21:
    print('****************The Match is tie !!****************')
    exit()


def dealer_choice():
    if sum(d_cards) < 17:
        while sum(d_cards) < 17:
            random.shuffle(deck)
            d_cards.append(deck.pop())

    print('Dealer has total ' + str(sum(d_cards)) + ' with the cards ',
          d_cards)

    if sum(p_cards) == sum(d_cards):
        print('****************The Match is tie !!****************')
        exit()

    if sum(d_cards) == 21:
        if sum(p_cards) < 21:
            print('****************Dealer is the Winner !!****************')
        elif sum(p_cards) == 21:
            print('****************The Match is tie !!****************')
        else:
            print('****************Dealer is the Winner !!****************')
    elif sum(d_cards) < 21:
        if sum(p_cards) < 21 and sum(p_cards) < sum(d_cards):
            print('****************Dealer is the Winner !!****************')
        if sum(p_cards) == 21:
            print('****************Player is the Winner !!****************')
        if sum(p_cards) < 21 and sum(p_cards) > sum(d_cards):
            print('****************Player is the Winner !!****************')
    else:
        if sum(p_cards) < 21:
            print('****************Player is the Winner !!****************')
        elif sum(p_cards) == 21:
            print('****************Player is the Winner !!****************')
        else:
            print('****************Dealer is the Winner !!****************')


while sum(p_cards) < 21:
    k = input('Want to hit or stay\n Press 1 for hit and 0 for stay. ')
    if k == 1:
        random.shuffle(deck)
        p_cards.append(deck.pop())
        print('You have total of ' + str(sum(p_cards)) + ' with the cards.',
              p_cards)
        if sum(p_cards) > 21:
            print(
                '*************You are BUSTED !*************\n Dealer Wins !!')
        if sum(p_cards) == 21:
            print(
                '*******************You are the Winner !!*****************************'
            )
    else:
        dealer_choice()
        break
