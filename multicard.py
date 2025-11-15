def validate_multi_card_play(selected_cards, current_value, player_hand):
    """
    Validates whether the player can legally play multiple cards at once.
    
    Parameters:
        selected_cards (list of int): The card values the player wants to play.
        current_value (int or None): The value currently on the pile (None if opening the round).
        player_hand (list of int): The full list of card values in the player's hand.

    Returns:
        bool: True if the play is valid, False otherwise.
    """

    # Step 1: Check if player is trying to play cards they don't actually have
    for card in selected_cards:
        if card not in player_hand:
            return False  # Trying to play a card not in hand

    # Step 2: Check that all selected cards match each other
    # (iteration + conditional logic)
    first_value = selected_cards[0]
    for card in selected_cards:
        if card != first_value:
            return False  # Cards do not match

    # Step 3: Check if the play matches or beats the current value on the pile
    # (game rule: must match or beat the existing value)
    if current_value is not None:
        if first_value < current_value:
            return False  # Play is too low to be legal

    # Step 4: If all conditions pass, the move is valid
    return True

def mock_run_tests():
    """ sample tests using fake data to demonstrate the function works """

    print("Test 1: Valid play (8,8 >= 7):")
    print(validate_multi_card_play([8, 8], 7, [8, 8, 10, 3]))  # Expected True

    print("Test 2: Invalid play (5,5 < 7):")
    print(validate_multi_card_play([5, 5], 7, [5, 5, 9])) 
    
# Only run mock tests if the file is run directly (not imported)
if __name__ == "__main__":
    mock_run_tests()