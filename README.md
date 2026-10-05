# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

This project started with an AI-generated Streamlit number guessing game that looked functional but contained several bugs.

The main problems were:

- The attempt counter started at 1 instead of 0.
- The Higher/Lower hints were reversed.
- The secret number was sometimes converted into a string, causing a `TypeError`.
- Some reusable game logic was mixed directly into `app.py`.

The goal was to reproduce the bugs, identify their causes, fix them, refactor reusable logic, and verify the results with manual testing and pytest.

---

## 🛠️ Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:

```bash
python -m streamlit run app.py
```

3. Run the automated tests:

```bash
python -m pytest
```

---

## 🐛 Bugs Found and Fixed

### 1. Attempt Counter Started Incorrectly

On Normal difficulty, the game should begin with 8 attempts available.

**Expected:**

```text
Attempts: 0
Attempts left: 8
```

**Actual:**

```text
Attempts: 1
Attempts left: 7
```

The issue was caused by the attempt counter being initialized to `1`.

**Fix:**

```python
st.session_state.attempts = 0
```

---

### 2. Higher and Lower Hints Were Reversed

During testing, the secret number was `19`.

When I guessed `10`, the game incorrectly displayed:

```text
Go LOWER!
```

The correct response should have been:

```text
Go HIGHER!
```

When I guessed `30`, the game incorrectly displayed:

```text
Go HIGHER!
```

The correct response should have been:

```text
Go LOWER!
```

The logic was corrected so that:

- Guess below the secret → `📈 Go HIGHER!`
- Guess above the secret → `📉 Go LOWER!`
- Correct guess → `🎉 Correct!`

---

### 3. Secret Number Type Error

The game sometimes converted the secret number from an integer into a string.

This caused comparisons such as:

```python
20 > "55"
```

and produced:

```text
TypeError: '>' not supported between instances of 'int' and 'str'
```

The unnecessary string conversion was removed so the secret number remains an integer during comparisons.

---

## 🔧 Refactoring

Reusable game logic was moved into `logic_utils.py`.

The refactored functions include:

- `check_guess()`
- `parse_guess()`

This made the core logic easier to test independently from the Streamlit interface.

For example:

```python
outcome, message = check_guess(60, 50)
```

returns:

```text
Too High
📉 Go LOWER!
```

---

## 📸 Demo Walkthrough

1. Start the Streamlit application.
2. Select Normal difficulty.
3. The game begins with 8 attempts available.
4. Open **Developer Debug Info** to view the secret number, attempts, score, difficulty, and history.
5. Enter a guess lower than the secret number.
6. The game displays `📈 Go HIGHER!`.
7. Enter a guess higher than the secret number.
8. The game displays `📉 Go LOWER!`.
9. The game also displays Cold, Warm, or Very Hot feedback based on how close the guess is to the secret.
10. Enter the correct number.
11. The game displays `🎉 Correct!` and shows the final score.

---

## 🧪 Test Results

The project was tested with pytest.

```text
============================= test session starts ==============================
collected 6 items

tests/test_game_logic.py ......                                   [100%]

============================== 6 passed in 0.01s ===============================
```

The tests cover:

- Winning guess
- Guess too high
- Guess too low
- Non-numeric input
- Empty input
- Negative number parsing

---

## 🚀 Stretch Features

### ✅ Advanced Edge-Case Testing

Additional pytest cases were added for:

- Non-numeric input
- Empty input
- Negative numbers

These tests verify that unusual or invalid input is handled without crashing the program.

The prompts and reasoning used for these tests are documented in `ai_interactions.md`.

---

### ✅ Professional Documentation and Style

`logic_utils.py` was improved with:

- Professional docstrings
- Argument descriptions
- Return-value descriptions
- Type hints
- Cleaner formatting
- PEP 8 style checks

The following command was used:

```bash
python -m pycodestyle logic_utils.py
```

The final style check returned no violations.

---

### ✅ Enhanced Game UI

The game was improved with distance-based feedback.

The player now receives:

- 🧊 **Cold** — the guess is far away
- 🌤️ **Warm** — the guess is getting closer
- 🔥 **Very Hot** — the guess is within 5 of the secret number

The original Higher/Lower hints still work alongside the new distance feedback.

Example:

```text
📈 Go HIGHER!
🧊 Cold! You're still far away.
```

or:

```text
📉 Go LOWER!
🔥 Very hot! You're extremely close.
```

---

## 🤖 AI Collaboration

AI was used as a debugging and development teammate throughout the project.

AI helped with:

- Investigating bugs
- Explaining Streamlit session state
- Refactoring game logic
- Designing pytest cases
- Creating edge-case tests
- Reviewing documentation
- Reviewing PEP 8 style
- Suggesting UI improvements

AI suggestions were not accepted automatically.

For example, an early interpretation suggested that submitting a guess after winning was incorrectly increasing the attempt count. After reviewing the Developer Debug Info and history more carefully, I realized the displayed state was stale and that other bugs were responsible for the main problems.

This showed the importance of verifying AI suggestions with actual application behavior and tests.

More details are documented in:

- `reflection.md`
- `ai_interactions.md`

---

## 📂 Project Files

### `app.py`

Contains:

- Streamlit interface
- Difficulty selection
- Session state
- Game flow
- Attempt handling
- Score handling
- Hot/Warm/Cold feedback

### `logic_utils.py`

Contains reusable logic including:

- `parse_guess()`
- `check_guess()`

### `tests/test_game_logic.py`

Contains pytest tests for:

- Winning guesses
- Too-high guesses
- Too-low guesses
- Non-numeric input
- Empty input
- Negative numbers

### `reflection.md`

Documents:

- Bugs found
- Expected vs actual behavior
- AI collaboration
- Testing process
- Streamlit state lessons
- Developer habits learned from the project

### `ai_interactions.md`

Documents:

- AI prompts
- Edge-case testing rationale
- Documentation and style improvements
- Verification steps

---

## ✅ Final Status

- [x] Game runs successfully in Streamlit
- [x] Attempt counter fixed
- [x] Higher/Lower hints fixed
- [x] Secret-number type issue fixed
- [x] Core logic refactored
- [x] 6 automated tests passing
- [x] Advanced edge-case tests added
- [x] Professional docstrings added
- [x] PEP 8 style check passing
- [x] Hot/Warm/Cold UI feedback added
- [x] Reflection completed
- [x] AI interaction documentation completed
- [x] Multiple meaningful Git commits created