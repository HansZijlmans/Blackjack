from enum import Enum
from random import randint,shuffle

class Card():
    possible_suits = [('Heart',1), ('Diamond',2), ('Spade',3), ('Club',4)]
    possible_values = [('Ace',1),('Two',2),('Three',3),('Four',4),('Five',5),
     ('Six',6),('Seven',7), ('Eight',8), ('Nine',9), ('Ten',10),
     ('Jack',10), ('Queen',10),('King',10)]
    
    def __init__(self, card_value = 0, suit = 0):
        self.card_value = Card.possible_values[card_value]
        self.suit = Card.possible_suits[suit]

class Entity():
    def __init__(self, bank_account = 0, name = 'blank'):
        self.bank_account = bank_account
        self.name = name
        self.cards = []
    
    def deposit(self, amount):
        self.bank_account += amount

    def compute_card_value(self):
        total_value = 0
        for card in self.cards:
            total_value += card.card_value[1]
        return total_value
    
    def print_current_cards(self):
        print('Current cards are')
        for card in self.cards:
            print(f'Card: {card.card_value[0]}, of {card.suit[0]}')
        print(f'Total value of the cards is {self.compute_card_value()}')

def generate_deck():
    deck = []
    order = list(range(1,52))
    shuffle(order)
    for i in order:
        card = Card(i % 13, i % 4)
        deck.append(card)
    
    return deck

def play_game(player, house, deck):
    player.cards.append(deck.pop())
    player.cards.append(deck.pop())
    player.print_current_cards()
    
    while True:
        action = input('What will be your action (hit / pass)?')
        if action == 'hit':
            player.cards.append(deck.pop())
            player.print_current_cards()
        
        elif action == 'pass':
            player.print_current_cards()
            break

        if player.compute_card_value() > 21:
            player.print_current_cards()
            print('Bust')
            break

    
def main():
    deck = generate_deck()
    print('Do you want to deposit some money?')
    money = int(input())
    player = Entity(bank_account = money,name = 'Player1')
    house = Entity(bank_account = 10**6, name = "House")
    play_game(player,house,deck)

if __name__ == '__main__':
    main()

