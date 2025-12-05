import random
class Player():
    pass
class ComputerPlayer():
    # Inherits from Player Class
    pass
class Main():
    """
    Card deck 
    Use Format Card Name : Value (Ex: "(A): 1)
    dictionary for Kings(K), Aces(A), Jack(J), Q(Queen)
    """
    pass
# Create Deck
card_values = {"A": 1, "2":2, "3":3, "4": 4, "5":5, "6":6, "7":7, "8":8, "9":9,\
    "K":10, "J": 11, "Q": 12}
deck = []
for card in card_values:
    for __ in range(4): 
        deck.append(card)
deck.random.shuffle()
# Main Game Loop




#

