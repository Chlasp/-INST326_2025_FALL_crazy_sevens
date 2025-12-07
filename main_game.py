import random
# Classes
class Player():
    def __init__(self):
        self.hand = []
class ComputerPlayer(Player):   
    def turn(self, last_card, round):
        """Runs a computer player's turn 

        Args:
            computer_player (Computer): Computer player object
            last_card (int): value of the last card played in the game
            round (int): current round in the game
        Side Effects:
            Updates computer_player.hand removing cards played this turn
        Raises:
            None
        Returns:
            None
        """
    # Initalizes computer player hand
        hand = self.hand
    
    # Creates playable card options
        playable_hand = [card for card in sorted(hand) \
            if card > last_card]
        if not playable_hand:
            return None
    # Checks for double hand
        count = {}
        for card in playable_hand:
            count[card] = count.get(card, 0) + 1
        double_hand = [card for card in playable_hand if count[card] > 1]
        if round == 3:
            if double_hand:
                chosen = double_hand[0]
                self.hand = [x for x in playable_hand if x != chosen]
            chosen = playable_hand[0]
            self.hand = [x for x in playable_hand if x != chosen]
        else:
            if (playable_hand[0] - last_card) < 3:
                chosen = playable_hand[0]
                self.hand = [x for x in playable_hand if x != chosen]
            else:
                chosen = double_hand[0]
                self.hand = [x for x in playable_hand if x != chosen]

# General Functions
def mock_is_valid_play(card, current_highest):
    """
    This mock just returns True if card > current_highest.
    """
    if current_highest is None:
        return True
    return card > current_highest

def choose_playable_card(hand, current_highest_card):
    """
    Determines which card a player should play next.
    Parameters:
        hand (list of ints): the player's current cards
        current_highest_card (int or None): highest card played in this round
    Returns:
        The lowest valid playable card, or None if no card can beat the current card.
    """
    sorted_hand = sorted(hand)
    
    for card in sorted_hand:
        if mock_is_valid_play(card, current_highest_card):
            return card
    return None

# Main Functions
class Main():
    """
    Card deck 
    Use Format Card Name : Value (Ex: "(A): 1)
    dictionary for Kings(K), Aces(A), Jack(J), Q(Queen)
    """
    pass
    # Create Deck
    card_values = {"A": 1, "2":2, "3":3, "4": 4, "5":5, "6":6, "7":7, "8":8, "9":9,\
        "K":13, "J": 12, "Q": 11}
    deck = []
    for card in card_values:
        for __ in range(4): 
            deck.append(card)
    random.shuffle(deck)
    # Main Game Loop
    player = Player()
    computer_player = ComputerPlayer()
    last_card = None
    for __ in range(7):
        player.hand.append(deck.pop())
        computer_player.hand.append(deck.pop())
    
    
    print("---- Welcome User Message ----")
    

