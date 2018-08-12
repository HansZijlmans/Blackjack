from enum import Enum
from random import randint,shuffle

class Card():
    possible_suits = [('Heart',1), ('Diamond',2), ('Spade',3), ('Club',4)]
    possible_values = [('Ace',11),('Two',2),('Three',3),('Four',4),('Five',5),
     ('Six',6),('Seven',7), ('Eight',8), ('Nine',9), ('Ten',10),
     ('Jack',10), ('Queen',10),('King',10)]
    
    def __init__(self, card_value = 0, suit = 0):
        self.card_value = Card.possible_values[card_value]
        self.suit = Card.possible_suits[suit]

class Entity():
    def __init__(self, bank_account = 0, entity_name = 'name'):
        self.bank_account = bank_account
        self.entity_name = entity_name
        self.cards = []
    
    def deposit(self, amount):
        self.bank_account += amount

    def compute_card_value(self):
        total_value = 0
        for card in self.cards:
            total_value += card.card_value[1]
        
        if total_value > 21:
            for card in self.cards:
                if card.card_value[0] == "Ace":
                    total_value -= 10
                if total_value < 21:
                    break

        return total_value
    
    def print_current_cards(self):
        print('---------------------------------')
        print(f'{self.entity_name}s current cards are')
        for card in self.cards:
            print(f'Card: {card.card_value[0]}, of {card.suit[0]}')
        print(f'Total value of the cards is {self.compute_card_value()}')
        print('---------------------------------')

def generate_deck():
    deck = []
    order = list(range(1,52))
    shuffle(order)
    for i in order:
        card = Card(i % 13, i % 4)
        deck.append(card)
    
    return deck

def deal_card(player, deck):
    player.cards.append(deck.pop())

def check_winner(player, house, bet):
    if house.compute_card_value() > 21:
        print('Player has won')
        player.deposit(bet)

    elif player.compute_card_value() > house.compute_card_value():
        print('Player has won')
        player.deposit(bet)
    else:
        print('House has won')
        player.deposit(-bet)  

def play_game(player, house, deck, bet):
    deal_card(house, deck)
    deal_card(player, deck)
    deal_card(player, deck)
    player.print_current_cards()
    house.print_current_cards()
    bust = False
    while True:
        action = input('What will be your action (hit / pass)?')
        if action == 'hit':
            deal_card(player, deck)
            player.print_current_cards()
        
        elif action == 'pass':
            player.print_current_cards()
            break

        if player.compute_card_value() > 21:
            player.print_current_cards()
            print('Bust')
            bust = True
            break
    
    if bust:
        player.deposit(-bet)
    else:
        while house.compute_card_value() < 17:
            deal_card(house, deck)

    house.print_current_cards()
    
    if not bust:
        check_winner(player, house, bet)

    print(f'Total player money = {player.bank_account}')

    
def main():
    print()
    money = int(input('How much do you want to deposit?'))
    player = Entity(bank_account = money,entity_name = 'Player1')
    house = Entity(bank_account = 10**6, entity_name = "House")
    stop = False
    while not stop:
        deck = generate_deck()
        player.cards = []
        house.cards = []
        bet = int(input('How much do you want to bet?'))
        play_game(player,house,deck,bet)
        want_to_stop = input('Stop y = stop?')
        if want_to_stop == "y":
            stop = True
    

if __name__ == '__main__':
    main()

