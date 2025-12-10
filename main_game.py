import random

class Main():
    """
    Card deck 
    Use Format Card Name : Value (Ex: "(A): 1)
    dictionary for Kings(K), Aces(A), Jack(J), Q(Queen)
    """
    pass
    # Create Deck"
    def __init__(self):
        self.card_values = {"A": 1, "2":2, "3":3, "4": 4, "5":5, "6":6, "7":7, "8":8, "9":9,
        "K":13, "J": 12, "Q": 11}
        self.deck = []
        for card in self.card_values:
            for __ in range(4): 
                self.deck.append(card)
        random.shuffle(self.deck)
    # Main Game Loop
        self.player = Player()
        self.computer_player = ComputerPlayer(self.card_values)
        self.last_card = None
        for __ in range(7):
           self. player.hand.append(self.deck.pop())
           self. computer_player.hand.append(self.deck.pop())
# Game loop
    def play_game(self):
        round = 1
        game_over = False
        
        while not game_over:
            print(f"\n--- Round {round} ---")
            print(f"Current highest card: {self.last_card}")
            print(f"Your hand:{self.player.hand}")
            
            player_hand = [self.card_values[card] for card in self.player.hand]
            last_card_value = self.card_values[self.last_card] if self.last_card else None
            
            playable_card_value = choose_playable_card(player_hand, last_card_value)
            playable_card = None
            
            if playable_card_value is not None:
            # Find the actual card to play
                playable_card = next(card for card in self.player.hand 
                                    if self.card_values[card] == playable_card_value)
                
            if playable_card is None:
                print("You have no playable cards. Computer cooked you!")
                game_over = True
                break
            
            playable_card = next(card for card in self.player.hand 
                           if self.card_values[card] == playable_card_value)
            print(f"You play: {playable_card}")
            self.player.hand.remove(playable_card)
            self.last_card = playable_card
            
            if not self.player.hand:
                print("Congratulations! You won!")
                game_over = True 
                break
            
            print("Computer's turn...")
            self.computer_player.turn(self.last_card, round)
            
            if not self.computer_player.hand:
                print("Computer wins!")
                game_over = True
                break
            
            round += 1
        
# Game loop functions
def is_valid_play(card, current_highest):
    """
    This just returns True if card > current_highest.
    
    Args:
        card(int): value of the card to play
        current_highest (int or None): value of the current highest card.
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
        if is_valid_play(card, current_highest_card):
            return card
    return None
# Classes
class Player():
    def __init__(self):
        self.hand = []
class ComputerPlayer(Player):  
    def __init__(self, card_values):
        super().__init__()
        self.card_values = card_values 
        
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
        if last_card == None:
            last_card = 0
    
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

def get_card_value(card):
    """Returns value of card.

    Args:
        card (str): String representation of the card(i.e 'A', '2', 'K')
    Returns:
        int: Number value of the card(i.e 2)
    """
    card_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7":  7,\
        "8": 8, "9": 9,"K":13, "J": 12, "Q": 11}
    return card_values[card]


    
if __name__ == "__main__":
    game = Main()
    game.play_game()