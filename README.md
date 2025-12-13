# Card Game: Multi-Card Play with Computer Opponent

## Repository Overview

This repository contains a Python-based card game where a human player competes against a computer opponent. Players can play one or more matching cards per turn, and special rules like swapping hands when multiple sevens are played are included.  

### Files in the Repository

| File | Purpose |
|------|---------|
| `main_game.py` | Contains the main game logic, including the `Main` class, player classes, and all functions for gameplay, input validation, and computer decision-making. |
| `multicard.py` | Contains the `validate_multi_card_play` function used to enforce multi-card rules for human and computer players. |

---

## How to Run the Program

1. Ensure Python 3.8+ is installed.  
2. Open a terminal or command prompt in the directory containing `main_game.py` and `multicard.py`.  
3. Run the program:

```bash
python main_game.py
```
## How to Play

1. **Starting Hand**: Each player (human and computer) receives 8 cards. Cards are represented as:  
   - `A` = Ace  
   - `2–10` = numeric cards  
   - `J` = Jack  
   - `Q` = Queen  
   - `K` = King  

2. **Player Turn**:  
   - Displayed hand shows all cards you currently hold.  
   - Choose **one card** (e.g., `7`) or **multiple matching cards** (e.g., `7 7`) to play.  
   - Only cards higher than the current highest card are valid, unless starting a new round.  
   - Type `QUIT` at any prompt to exit the game.  

3. **Computer Turn**:  
   - The computer waits 1 second (“thinking”) before playing a card.  
   - The computer chooses the lowest valid card that follows its strategy, with preference for doubles when applicable.  

4. **Winning Conditions**:  
   - First player to play all cards wins.  
   - If a player cannot play a valid card, they lose the round.  

---

## Interpreting Output

- **Current Highest Card**: Shows the last card played by either player.  
- **Playable Cards**: Shows cards in your hand that can legally be played this turn.  
- **Computer Plays**: Displays the card played by the computer.  
- **Hand Swap Notification**: If two or more sevens are played, the hands of the two players are swapped.  

## Annotated Bibliography
 1. **Python `time` Module Documentation**  
   - Source: [https://docs.python.org/3/library/time.html](https://docs.python.org/3/library/time.html)  
   - Used to implement the computer “thinking” delay (`time.sleep(1)`).  

---
