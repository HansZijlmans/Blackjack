class Card():
    pass

class Player():
    def __init__(self, bank_account = 0):
        self.bank_account = bank_account
    
    def deposit(self, amount):
        self.bank_account += amount

