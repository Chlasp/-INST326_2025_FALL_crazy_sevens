#Computer Player will be an object with a current deck of cards
import random
import math
def computer_turn(computer_player, last_card, round):
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
    hand = computer_player.hand
    
    # Creates playable card options
    playable_hand = [card for card in sorted(hand) \
        if card > last_card]
    if not playable_hand:
        return None
    # Count occurences of each card and check and make a list for doubles
    # Doubles are card values that occur more than once
    count = {}
    for card in playable_hand:
        count[card] = count.get(card, 0) + 1
    double_hand = [card for card in playable_hand if count[card] > 1]
    """
    Logic:
    If it is currently round three, then immediatly check for doubles.
    If there are no doubles, than look for the lowest value in
    the playable hand. 
    If it is round 2 or less, look first to see if the closest card is within 
    three values of the target. If it is not then look for double cards first.
    
    """
    if round == 3:
        if double_hand:
            chosen = double_hand[0]
            computer_player.hand = [x for x in playable_hand if x != chosen]
        chosen = playable_hand[0]
        computer_player.hand = [x for x in playable_hand if x != chosen]
    else:
        if (playable_hand[0] - last_card) < 3:
            chosen = playable_hand[0]
            computer_player.hand = [x for x in playable_hand if x != chosen]
        else:
            chosen = double_hand[0]
            computer_player.hand = [x for x in playable_hand if x != chosen]
    