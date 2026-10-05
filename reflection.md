# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, the interface looked normal, but the internal game logic had several problems. The game started with 7 attempts left even though Normal difficulty allowed 8 attempts, because the attempts counter was initialized at 1 instead of 0. The HIGHER and LOWER hints were also reversed, so guessing below the secret told me to go lower instead of higher. I later found another bug where the secret number was sometimes converted from an integer to a string, causing a TypeError during comparison.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Start a new Normal game | 8 attempts left and attempts = 0 | Game showed 7 attempts left and attempts = 1 | No console error |
| Secret = 19, guess = 10 | Go HIGHER | Go LOWER | No console error |
| Secret = 19, guess = 30 | Go LOWER | Go HIGHER | No console error |
| Secret = 55, guess = 20 | Compare two integers and return a hint | Secret was converted to a string and comparison failed | `TypeError: '>' not supported between instances of 'int' and 'str'` |

---

## 2. How did you use AI as a teammate?

I used ChatGPT as an AI teammate to help inspect the behavior, locate likely bugs, refactor the code, and create tests. One correct suggestion was to move `check_guess()` into `logic_utils.py` and fix the reversed hint messages so a high guess says "Go LOWER" and a low guess says "Go HIGHER." I verified that suggestion manually in Streamlit and then with pytest, where all three tests passed. One suggestion I did not accept as written was the initial assumption that submitting a guess after winning was incorrectly increasing the attempt count; after checking the debug panel and history more carefully, I realized the displayed state was stale and the more important problems were the attempt initialization and the secret being converted to a string.

---

## 3. Debugging and testing your fixes

I considered a bug fixed only after I could reproduce the original problem and then confirm that the same scenario behaved correctly after the change. For example, after fixing `check_guess()`, I tested a guess below the secret and confirmed that the game returned "Go HIGHER," then tested a guess above the secret and confirmed that it returned "Go LOWER." I also ran `python -m pytest`, and all three tests passed, including tests for a winning guess, a guess that was too high, and a guess that was too low. AI helped me understand how to structure the tests around the tuple returned by `check_guess()` instead of comparing the entire result directly to a string.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the Python script when the user interacts with the app, so values that need to survive between reruns must be stored in `st.session_state`. I would explain session state as a small memory area that keeps important values such as the secret number, attempts, score, status, and history while the page reruns. I also learned that the order in which the page is rendered and state is updated can make displayed values look temporarily stale. This made me realize that debugging Streamlit requires checking both the UI and the underlying session state.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is reproducing a bug with a specific input before changing the code, then testing the exact same scenario after the fix. I also want to keep using small Git commits so each repair is documented separately and is easier to review or undo. Next time I work with AI, I would verify its interpretation sooner instead of assuming its first explanation of a bug is correct. This project changed the way I think about AI-generated code because code can look reasonable and still contain subtle logic, state, and type errors, so human verification is still essential.