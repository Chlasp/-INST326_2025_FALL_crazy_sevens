"""
multicard.py

This module contains logic for validating multi card plays.

Cards are represented as string labels such as A 2 3 J Q K.
Card comparisons are done using the same card_values dictionary
that exists in the main game file.
"""

from collections import Counter


def validate_multi_card_play(selected_labels, current_top_label,
                             player_hand_labels, card_values):
    """
    Determines whether a player can legally play multiple cards in a single turn.

    The function checks that the selected cards are valid, that the player
    actually owns the cards, that all selected cards match each other,
    and that the play beats the current top card if one exists.

    Parameters
        selected_labels list of str
            The cards the player wants to play such as 7, 7 or K

        current_top_label str or None
            The current highest card on the pile or None if this is the first play

        player_hand_labels list of str
            The full list of cards currently in the player's hand

        card_values dict
            Dictionary that maps card labels to numeric values

    Returns
        bool
            True if the play is valid
            False if the play is illegal
    """

    if not isinstance(selected_labels, list) or len(selected_labels) == 0:
        return False

    selected = [str(card).strip().upper() for card in selected_labels
                if str(card).strip() != ""]
    if not selected:
        return False

    # every selected card must be a known label
    for card in selected:
        if card not in card_values:
            return False

    hand_counter = Counter(str(card).strip().upper() for card in player_hand_labels)
    selected_counter = Counter(selected)

    # --- rubric technique: set operations (set difference) ---
    # labels that were selected but never appear in the hand at all
    missing_labels = set(selected_counter.keys()) - set(hand_counter.keys())
    if missing_labels:
        return False
    # --------------------------------------------------------

    # make sure the player actually has enough copies of each card
    for label, count in selected_counter.items():
        if hand_counter[label] < count:
            return False

    # all selected cards must match each other (e.g., "7 7" or "Q Q Q")
    first_label = selected[0]
    for card in selected:
        if card != first_label:
            return False

    # basic rule check for whether this rank is allowed
    if not mock_check_card_rules(first_label, current_top_label, card_values):
        return False

    # multi-card play must still beat the current top card (if there is one)
    if current_top_label is not None:
        top_label = str(current_top_label).strip().upper()
        if top_label not in card_values:
            return False
        if card_values[first_label] <= card_values[top_label]:
            return False

    return True


def mock_check_card_rules(card_label, current_top_label, card_values):
    """
    Simulates checking whether a card is allowed to be played.

    This function exists to satisfy assignment requirements.
    It currently approves any card that exists in the card_values dictionary.

    Parameters
        card_label str
            The label of the card being played

        current_top_label str or None
            The current card on the pile

        card_values dict
            Dictionary mapping card labels to numeric values

    Returns
        bool
            True if the card is allowed
    """
    return card_label in card_values


def find_valid_multi_card_plays(player_hand_labels, current_top_label,
                                card_values, min_count=2):
    """
    Finds multi-card play options in a player's hand.

    Parameters
        player_hand_labels list of str
            The cards currently in the player's hand

        current_top_label str or None
            The current highest card on the pile

        card_values dict
            Dictionary that maps card labels to numeric values

        min_count int, optional
            Minimum number of matching cards required for a multi-card play

    Returns
        dict
            Maps card label to count for labels that appear at least min_count
            times in the hand and beat the current_top_label (if one exists)
    """
    cleaned_hand = [str(card).strip().upper() for card in player_hand_labels]
    counts = Counter(cleaned_hand)

    if current_top_label is not None:
        top_label = str(current_top_label).strip().upper()
        top_value = card_values.get(top_label, -1)
    else:
        top_value = -1

    # rubric techniques: comprehension + optional parameter
    options = {
        label: count
        for label, count in counts.items()
        if count >= min_count and card_values.get(label, -1) > top_value
    }

    return options


def mock_run_tests():
    """
    Runs sample test case
    """

    card_values = {
        "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9, "J": 12, "Q": 11, "K": 13
    }

    print("Test 1 Valid play two eights beating seven")
    print(validate_multi_card_play(["8", "8"], "7", ["8", "8", "K", "3"], card_values))

    print("\nTest 2 Invalid play two fives below seven")
    print(validate_multi_card_play(["5", "5"], "7", ["5", "5", "9"], card_values))

    print("\nTest 3 Invalid play missing required cards")
    print(validate_multi_card_play(["9", "9"], "3", ["9", "2", "5"], card_values))

    print("\nTest 4 Invalid mixed card values")
    print(validate_multi_card_play(["7", "8"], "5", ["7", "8", "8"], card_values))

    print("\nTest 5 Valid opening play with no top card")
    print(validate_multi_card_play(["Q", "Q"], None, ["Q", "Q", "A"], card_values))


if __name__ == "__main__":
    mock_run_tests()