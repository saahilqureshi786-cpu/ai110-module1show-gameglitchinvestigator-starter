from logic_utils import check_guess


def test_winning_guess():
    outcome, message = check_guess(50, 50)

    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)

    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)

    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

from logic_utils import parse_guess


def test_non_numeric_input():
    ok, guess, error = parse_guess("hello")

    assert ok is False
    assert guess is None
    assert error == "That is not a number."


def test_empty_input():
    ok, guess, error = parse_guess("")

    assert ok is False
    assert guess is None
    assert error == "Enter a guess."


def test_negative_number():
    ok, guess, error = parse_guess("-5")

    assert ok is True
    assert guess == -5
    assert error is None