import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')

random.shuffle(deck)

def deal(deck, hand):
    card = deck.pop()
    hand.append(card)

def calculate_hand_value(hand):
    value=0
    has_ace = False

    for card in hand:
        rank = card.split()[0]
        value += values[rank]
        if rank == 'Ace':
            has_ace = True
    # the forbidden wild card. 
    if has_ace and value > 21:
        value -= 10
    return value

player_hand=[]
dealer_hand=[]

deal(deck, player_hand)
deal(deck, player_hand)
deal(deck, dealer_hand)
deal(deck, dealer_hand)

while True:
    print(f'Player hand: {player_hand} ({calculate_hand_value(player_hand)})')
    print(f'Dealer hand: [{dealer_hand[0]}, <face down>]')

    if calculate_hand_value(player_hand) > 21:
        print('Busted! You lose.')
        break
            
    action = input('do you want to hit or stand? ')

    if action.lower() == 'hit':
        deal(deck, player_hand)
    if action.lower() == 'stand':
        print(f'player hand: {player_hand}({calculate_hand_value(player_hand)})')
        print(f'Dealer hand: {dealer_hand}({calculate_hand_value(dealer_hand)})')

        if calculate_hand_value(dealer_hand) > 21:
            print('Dealer busted! You win!')
        elif calculate_hand_value(player_hand) > 21:
            print('Busted! You lose.')        
        elif calculate_hand_value(dealer_hand) > calculate_hand_value(player_hand):
            print('Dealer wins! You lose.')
        elif calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
            print('You win!')
        else:
            print('Push!')

