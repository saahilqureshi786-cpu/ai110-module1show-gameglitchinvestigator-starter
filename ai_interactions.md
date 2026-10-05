# AI Interactions

## Challenge 1: Advanced Edge-Case Testing

### Prompt Used
Help me add pytest cases for edge-case inputs in the Game Glitch Investigator project. Test non-numeric input, empty input, and negative numbers using the parse_guess() function.

### Edge Cases Chosen

1. **Non-numeric input (`"hello"`)**
   - Chosen to verify that invalid text does not crash the game.
   - Expected result: return an error saying the input is not a number.

2. **Empty input (`""`)**
   - Chosen to verify that submitting no value is handled gracefully.
   - Expected result: return an "Enter a guess." error.

3. **Negative number (`"-5"`)**
   - Chosen to verify that numeric parsing still works for signed integers.
   - Expected result: successfully parse the value as `-5`.

### Verification
I ran:

`python -m pytest`

All six tests passed successfully.