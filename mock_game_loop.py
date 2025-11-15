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

hand = [3, 7, 9, 2]
current_highest = 6

result = choose_playable_card(hand, current_highest)
print(result)