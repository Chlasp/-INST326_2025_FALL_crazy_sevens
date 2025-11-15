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
        list: Returns a list of cards the player has run
    """
    # Dummy Values
    computer_player.hand = [7,8,8,8,9,10]
    playable_hand = [card for card in sorted(computer_player.hand) \
        if card > last_card]
    count = {}
    for card in playable_hand:
        count[card] = count.get(card, 0) + 1
    double_hand = [card for card in playable_hand if count[card] > 1]
    if round == 3:
        if double_hand:
            chosen = double_hand[0]
            computer_player.hand = [x for x in playable_hand if x != chosen]
            return [x for x in playable_hand if x == chosen]
        chosen = playable_hand[0]
        computer_player.hand = [x for x in playable_hand if x != chosen]
        return [x for x in playable_hand if x == chosen]
    else:
        if (playable_hand[0] - last_card) < 3:
            chosen = playable_hand[0]
            computer_player.hand = [x for x in playable_hand if x != chosen]
            return [x for x in playable_hand if x == chosen]
        else:
            chosen = double_hand[0]
            computer_player.hand = [x for x in playable_hand if x != chosen]
            return [x for x in playable_hand if x == chosen]
    