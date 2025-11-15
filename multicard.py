def validate_multi_card_play(selected_cards, current_value, player_hand):
    """
    Validates whether the player can legally play multiple cards at once.

    Parameters:
        selected_cards (list of int): The card values the player wants to play.
        current_value (int or None): The value currently on the pile (None if opening round).
        player_hand (list of int): The full list of card values in the player's hand.

    Returns:
        bool: True if the play is valid, False otherwise.
    """

    # Step 1: Check if player is trying to play cards they don't actually have
    for card in selected_cards:
        if card not in player_hand:
            return False  # Trying to play a card not in hand

    # Step 2: Check that all selected cards match each other
    first_value = selected_cards[0]
    for card in selected_cards:
        if card != first_value:
            return False  # Cards do not match

    # Step 2.5: Mock rule check (assignment requirement)
    if not mock_check_card_rules(first_value, current_value):
        return False

    # Step 3: Check if the play matches or beats the current value on the pile
    if current_value is not None:
        if first_value < current_value:
            return False  # Play is too low to be legal

    # Step 4: All conditions satisfied → valid play
    return True


def mock_check_card_rules(card_value, current_value):
    """
    Mock function that simulates checking whether a card is allowed to be played.
    For assignment purposes, it simply returns True as long as the value is an integer.
    """
    return isinstance(card_value, int)


def mock_run_tests():
    """ Sample tests using fake data to demonstrate the function works """

    print("Test 1: Valid play (8,8 >= 7):")
    print(validate_multi_card_play([8, 8], 7, [8, 8, 10, 3]))  # Expected True

    print("\nTest 2: Invalid play (5,5 < 7):")
    print(validate_multi_card_play([5, 5], 7, [5, 5, 9]))  # Expected False

    print("\nTest 3: Trying to play a card not in hand:")
    print(validate_multi_card_play([9, 9], 3, [9, 2, 5]))  # Expected False

    print("\nTest 4: Mixed-value cards (should fail):")
    print(validate_multi_card_play([7, 8], 5, [7, 8, 8]))  # Expected False


if __name__ == "__main__":
    mock_run_tests()