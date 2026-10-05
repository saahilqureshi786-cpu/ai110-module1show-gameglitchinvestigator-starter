def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """
    Return the inclusive number range for a game difficulty.

    Args:
        difficulty: Difficulty level selected by the player.

    Returns:
        A tuple containing the minimum and maximum allowed values.

    Raises:
        NotImplementedError: Until this logic is refactored from app.py.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )


def parse_guess(raw: str) -> tuple[bool, int | None, str | None]:
    """
    Parse raw user input into an integer guess.

    Args:
        raw: Text entered by the player.

    Returns:
        A tuple containing:
        - whether parsing succeeded
        - the parsed integer, or None
        - an error message, or None
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except (ValueError, TypeError):
        return False, None, "That is not a number."

    return True, value, None


# FIX: Refactored and corrected high/low hint logic with AI assistance.
def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """
    Compare a player's guess with the secret number.

    Args:
        guess: Number entered by the player.
        secret: Secret number the player is trying to guess.

    Returns:
        A tuple containing the outcome and user-facing hint message.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"
