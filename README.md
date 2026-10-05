# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

This project started with an AI-generated number guessing game built with Streamlit. The game looked functional at first, but testing revealed several logic and state-management bugs.

- The attempt counter started incorrectly.
- The Higher/Lower hints were reversed.
- The secret number was sometimes converted into a string, causing a `TypeError`.
- Some reusable game logic was still inside `app.py`.

## 🛠️ Setup

1. Install dependencies:

```bash
pip install -r requirements.txt