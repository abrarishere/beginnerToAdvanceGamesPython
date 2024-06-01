A detailed explanation of the `computer_turn` function:

```python
def computer_turn(structure):
    # Check if the computer can win in the next move
    for i in range(9):
        if structure[i] == ' ':
            structure[i] = 'O'
            if check_win(structure, 'O'):
                return i
            structure[i] = ' '  # Reset the position if it doesn't lead to a win

    # Block the player's winning move
    for i in range(9):
        if structure[i] == ' ':
            structure[i] = 'X'
            if check_win(structure, 'X'):
                structure[i] = 'O'  # Block the player
                return i
            structure[i] = ' '  # Reset the position if it doesn't block a win

    # Take the center position if available
    if structure[4] == ' ':
        return 4

    # Take any random empty position
    while True:
        move = random.randint(0, 8)
        if structure[move] == ' ':
            return move
```

### Step-by-Step Explanation

1. **Check if the computer can win in the next move:**
   ```python
   for i in range(9):
       if structure[i] == ' ':
           structure[i] = 'O'
           if check_win(structure, 'O'):
               return i
           structure[i] = ' '  # Reset the position if it doesn't lead to a win
   ```
   - The function iterates through each position on the board (from 0 to 8).
   - For each position, it checks if the position is empty (`' '`).
   - If it is empty, the computer temporarily places its marker (`'O'`) there.
   - Then, it checks if this move results in a win for the computer by calling `check_win`.
   - If it results in a win, the function returns this position as the computer's move.
   - If not, it resets the position back to empty (`' '`) and continues checking the next positions.

2. **Block the player's winning move:**
   ```python
   for i in range(9):
       if structure[i] == ' ':
           structure[i] = 'X'
           if check_win(structure, 'X'):
               structure[i] = 'O'  # Block the player
               return i
           structure[i] = ' '  # Reset the position if it doesn't block a win
   ```
   - If the computer cannot win in its next move, it then checks if the player can win in their next move.
   - Similar to the first step, it iterates through each position, temporarily placing the player's marker (`'X'`) to see if the player would win.
   - If placing `'X'` in a position results in a win for the player, the computer places its marker (`'O'`) there to block the player and returns that position.
   - If it doesn't block a win, it resets the position and continues checking.

3. **Take the center position if available:**
   ```python
   if structure[4] == ' ':
       return 4
   ```
   - If neither the computer nor the player is about to win, the computer prefers to take the center position (position 4) if it is available.
   - The center position is often a strategic spot in Tic-Tac-Toe.

4. **Take any random empty position:**
   ```python
   while True:
       move = random.randint(0, 8)
       if structure[move] == ' ':
           return move
   ```
   - If none of the above conditions are met, the computer selects a random empty position.
   - It continues generating random positions until it finds an empty one and returns that as its move.

This function ensures that the computer plays optimally by first trying to win, then blocking the opponent's winning move, and finally making a strategic or random move if no immediate threats or opportunities are present.
