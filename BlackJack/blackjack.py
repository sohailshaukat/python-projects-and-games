import random
from Deck import Deck,Card

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():

    def __init__(self):
        self.balance = 100
        self.bet = 0

    def win_bet(self):
        self.balance += self.bet

    def lose_bet(self):
        self.balance -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('[+]Place your bet (Your bet shouldn't exceed your balance): '))
        except ValueError:
            print("[-]Sorry, it has to be an integer value!")
        else:
            print("[+]Placing bet...")
            if chips.bet > chips.balance:
                print("[-]Insufficient Balance.. Your Current balance is {chip.balance}...")
            else:
                break

if "__name__" == "__main__":

    while True:
        print('Welcome to BlackJack!! Closest to 21 without going over 21 \nDealers hit until she reaches 17. Aces count as 1 or 11.')
        deck = Deck()
        print('[+]Shuffling the deck...')
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_chips = Chips()
        print(f"[+]You've got {player_chips.balance} chips")

        take_bet(player_chips)
