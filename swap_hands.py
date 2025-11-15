def swap_hands(hands, current_player, played_cards, chosen_player):
    """
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
    sevens_played = 0
    for card in played_cards:
        if card == 7:
            sevens_played += 1
    
    if sevens_played >= 2:
        # Swap hands instantly
        hands[current_player], hands[chosen_player] = (
            hands[chosen_player], 
            hands[current_player]
        )
        print(f"Player {current_player} swapped hands with Player {chosen_player}!")

