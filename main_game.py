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
        for __ in range(8):
           self.player.hand.append(self.deck.pop())
           self.computer_player.hand.append(self.deck.pop())
           
    def player_turn(self):
        print(f"\nYour hand: {self.player.hand}")
        print(f"Current highest card: {self.last_card}")
        
         # determine valid cards
        if self.last_card:
            last_value = self.card_values[self.last_card]
            valid_cards = [c for c in self.player.hand if self.card_values[c] > last_value]
        else:
            valid_cards = self.player.hand.copy()

        if not valid_cards:
            print("You have no playable cards. Computer cooked you!")
            return None

        print(f"Playable cards: {valid_cards}")

        # ask user for card
        while True:
            choice = input("Choose a card to play: ").strip().upper()

            if choice not in self.player.hand:
                print("You don't have that card. Try again.")
                continue

            if choice not in valid_cards:
                print("That card cannot be played. Choose a valid card.")
                continue

            self.player.hand.remove(choice)
            print(f"You play: {choice}")
            return choice
        
                 
# Game loop
    def play_game(self):
        round = 1
        game_over = False
        
        while not game_over:
            print(f"\n--- Round {round} ---")
    
            # Player turn
            player_card = self.player_turn()
            if player_card is None:
                game_over = True
                break
            
            self.last_card = player_card
            
            if not self.player.hand:
                print("Congratulations! You won!")
                game_over = True 
                break
            
            print("\nComputer's turn...")
            computer_card = self.computer_player.turn(self.last_card, round)
            
            if computer_card is None:
                print("Computer cannot play and loses!")
                break

            print(f"Computer plays: {computer_card}")
            self.last_card = computer_card
            
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
        last_card_value = self.card_values[last_card] if last_card else 0
        hand_values = [self.card_values[card] for card in self.hand]
    
    # Creates playable card options
        playable_hand = [card for card in hand_values \
            if card > last_card_value]
        if not playable_hand:
            return None
    # Checks for double hand
        count = {}
        for card in playable_hand:
            count[card] = count.get(card, 0) + 1
        double_hand = [card for card in playable_hand if count[card] > 1]
        if round == 3:
            chosen = double_hand[0] if double_hand else playable_hand[0]
        else:
            if (playable_hand[0] - last_card_value) < 3:
                chosen = playable_hand[0]
            else:
                chosen = double_hand[0] if double_hand else playable_hand[0]
              
        for card in self.hand:
            if self.card_values[card] == chosen:
                self.hand.remove(card)
                return card

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