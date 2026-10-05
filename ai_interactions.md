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

## Challenge 3: Professional Documentation and Style

### Prompt Used
Review `logic_utils.py` and improve the function documentation and PEP 8 style without changing the existing behavior. Add professional docstrings to all functions and keep the code simple and readable.

### Changes Applied
- Added detailed docstrings with arguments and return values.
- Added type hints to functions.
- Kept two blank lines between top-level functions.
- Moved the FIX comment next to the function it describes.
- Kept line lengths readable.
- Added a final newline to resolve the W292 style warning.

### Verification

I ran:

`python -m pytest`

Result:

```text
6 passed in 0.01s