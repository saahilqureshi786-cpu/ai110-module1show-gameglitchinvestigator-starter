# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number and test the game behavior.
2. **Find the State Bug.** Investigate how Streamlit session state stores the secret number, attempts, score, and history.
3. **Fix the Logic.** Correct the Higher/Lower hint behavior.
4. **Refactor & Test.**
   - Move the `check_guess()` logic into `logic_utils.py`.
   - Run `pytest` in the terminal.
   - Keep fixing until all tests pass.

## 📝 Document Your Experience

- [x] **Game purpose:** The game asks the player to guess a randomly generated secret number within a difficulty-based range.
- [x] **Bugs found:** The attempt counter started at 1 instead of 0, the Higher/Lower hints were reversed, and the secret was sometimes converted from an integer to a string, causing a `TypeError`.
- [x] **Fixes applied:** I corrected the hint logic, initialized attempts at 0, kept the secret value as an integer, refactored `check_guess()` into `logic_utils.py`, and verified the fixes with manual testing and pytest.

## 📸 Demo Walkthrough

1. The user starts a new game on Normal difficulty with 8 attempts available.
2. The Developer Debug Info shows the secret number, attempts, score, and history.
3. If the user enters a guess lower than the secret, the game displays `Go HIGHER!`.
4. If the user enters a guess higher than the secret, the game displays `Go LOWER!`.
5. When the user enters the correct number, the game displays `Correct!` and shows the final score.
6. The game tracks the player's guesses and updates the attempt count during play.

**Screenshot** *(optional)*: Add a screenshot of the fixed winning game here if desired.

## 🧪 Test Results

```text
============================= test session starts ==============================
collected 3 items

tests/test_game_logic.py ...                                      [100%]

============================== 6 passed in 0.XXs ==============================