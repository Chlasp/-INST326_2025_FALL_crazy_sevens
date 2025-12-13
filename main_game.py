import random
import time
from multicard import validate_multi_card_play, find_valid_multi_card_plays
import pandas as pd

class Main():
    """
    Card deck 
    Use Format Card Name : Value (Ex: "(A): 1)
    dictionary for Kings(K), Aces(A), Jack(J), Q(Queen)
    """
    pass
    # Create Deck"
    def __init__(self):
        """
        Primary Author: David
        Technique Claimed: comprehensions / generator expressions
        
        Initializes the card deck, shuffles it, creates player objects, 
        and deals starting hands to both Player and Computer Player.
        
        Side effects:
            Modifies self.deck
            Intializes self.player and self.computer_player hands
        """
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
        self.table = []
           
   
        
    def player_turn(self):
        """
        Primary Author: David
        
        Handles a single turn for Player.
        Displays Player's hand, determines playable cards,
        validates input for single or multi-card plays,
        and allows Player to quit the game.
        
        Returns:
            str or None:
                Card played
                "QUIT" if the player wants to exit game
                None if no valid move exists
        """
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
            
            # NEW: use Danica's helper to show multi-card options
        multi_options = find_valid_multi_card_plays(
            self.player.hand,
            self.last_card,
            self.card_values,
            min_count=2      # keyword argument for the optional parameter
        )
        if multi_options:
            print("Multi-card options (card: count):")
            print(multi_options)

        print(f"Playable cards: {valid_cards}")
        print("You may play 1 card or multiple *matching* cards (e.g., '8 8', 'K K').")

        # ask user for card
        while True:
            choice = input("Choose a card to play: ").strip().upper()
            
            if choice == "QUIT":
                return "QUIT"
            
            selected = choice.split()
            
            card_check = [c for c in selected if not c in self.player.hand]
            if card_check:
                print(f"You do not have these cards: {card_check}. Try again.")
                continue

            if not validate_multi_card_play(selected, self.last_card, self.player.hand, self.card_values):
                print("Not a valid play under multi card rules.")
                continue
            
            for c in selected:
                self.player.hand.remove(c)
            
            hands = [self.player.hand, self.computer_player.hand]
            
            swap_hands(hands, 0, selected, 1)
            self.player.hand = hands[0]
            self.computer_player.hand = hands[1]
            
            print(f"You play: {selected}")
            return selected[0]
    def store_data_table(self,player):
        win_percentage = round/player.wins
        player.table.append((round, winner, win_percentage))
                  
        winner = self.play_game()
        self.table.append((round, winner, win_percentage))
    
    
    
            
            
            
            
        
        
                 
# Game loop
    def play_game(self):
        """
        Primary Author: David
        Technique Claimed: f-strings containing expressions
        
        Runs the main game loop, alternating turns between human and computer.
        Uses f-strings to clearly display round information, player hand,
        and current highest card.
        Allows quitting and win/loss detection.
        
        
        Side effects:
            Prints game progress to console
            Updates game state variables like self.last_card
        """
        round = 1
        game_over = False
        winner = None
        
        while not game_over:
            print(f"\n--- Round {round} ---")
    
            # Player turn
            player_card = self.player_turn()
            
            if player_card == "QUIT":
                print("You quit the game.")
                game_over = True
                break
            
            if player_card is None:
                winner = "Computer"
                game_over = True
                break
            
            self.last_card = player_card
            
            if player_card == "K" and "K" in self.computer_player.hand:
                print("Computer has a K! Playing it immediately...")
                self.computer_player.hand.remove("K")
                computer_card = "K"
                print(f"Computer plays: {computer_card}")
            else:
                print("\nComputer's turn...")
                print("\nComputer is thinking...", end="", flush=True)
                print("\n")
                time.sleep(1)
                computer_card = self.computer_player.turn(self.last_card, round)
                if computer_card is None:
                    winner = "Player"
                    print("Computer cannot play and loses!")
                    break
                print(f"Computer plays: {computer_card}")
                self.last_card = computer_card
                
                if computer_card == "K" and "K" in self.player.hand:
                    print("You have a K! You can play it immediately...")
                    self.player.hand.remove("K")
                    player_card = "K"
                    print(f"You play: {player_card}")
                    self.last_card = player_card
                   
            if not self.player.hand:
                winner = "Player"
                print("Congratulations! You won!")
                game_over = True 
                break
    
            
            if not self.computer_player.hand:
                winner = "Computer"
                print("Computer wins!")
                game_over = True
                break
            
            round += 1
        return winner
    
    def session(self, max_games=None):
        game_count = 0
        self.results = {"Player": 0, "Computer": 0}
        
        while True:
            self.__init__()
            winner = self.play_game()
            if winner:
                self.results[winner] += 1
                
            game_count += 1
            if max_games and game_count >= max_games:
                break
            
            choice = input("Play another game? (y/n): ").strip().lower()
            if choice != "y":
                break
            
        print("\n=== Session Summary ===")
        print(f"Total games played: {game_count}")
        print(f"Player wins: {results['Player']}")
        print(f"Computer wins: {results['Computer']}")
        
# Game loop functions
def is_valid_play(card, current_highest):
    """
    Primary Author: David 
    
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
    Primary Author: David 
    
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

def swap_hands(hands, current_player, played_cards, chosen_player):
    """
    Primary Author: Miguel
    
    Swap hands if current player plays 2 or more 7's
    
    Args:
        hands (list ): list of player hands, each hand is a list of cards
        current_player (int): index of the player who played
        played_cards (list): list of cards the player played this turn
        chosen_player (int): index of the player to swap hands with
    
    Returns:
        None 
    """
    # Count how many 7s were played
    sevens_played = sum(1 for c in played_cards if c == "7")

    
    if sevens_played >= 2:
        # Swap hands instantly
        hands[current_player], hands[chosen_player] = (
            hands[chosen_player], 
            hands[current_player]
        )
        print(f"Player {current_player} swapped hands with Player {chosen_player}!")  
        return hands[current_player]       
# Game Tracking Functions
        
        
        
# Classes
class Player():
    def __init__(self):
        self.hand = []
        self.table = []
        self.name = "user"
        self.wins = 0
    
    
class ComputerPlayer(Player):  
    def __init__(self, card_values):
        super().__init__()
        self.name = "computer"
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
            if card > last_card_value and card - last_card_value  < 5]
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

if __name__ == "__main__":
    game = Main()
    game.session()