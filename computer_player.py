#Computer Player will be an object with a current deck of cards
import random
def computer_turn(computer_player, last_value):
    # Dummy Values
    computer_player.hand =({"Ace of Spades": random.choice(1 or 11),
                            "Seven of Hearts": 7, "Seven of Diamonds": 7,
                           "Six of Spades": 6, "King of Diamonds": 10})
    # TODO Sort Values only if they are above the card Value using List Comprehension. 
    playable_hand = [card for card in computer_player.hand
                            if card.value > last_value]
    if not playable_hand:
        return None
    # TODO check to see if any cards have duplicates
    
    # TODO Check to see if a card has three or more cards above card number + 3
    
    
     

# The cards are currently played in an ongoing round.
# The value of the more recently played card.
# The card with the highest value currently.
# Computer turn and hand content
