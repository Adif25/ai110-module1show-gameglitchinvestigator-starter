from __future__ import annotations


def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Return (low, high) inclusive range for a given difficulty.

    The original logic lived in `app.py`.  It was moved here as part of a
    refactor to separate game logic from the Streamlit UI.  Keeping it here
    makes unit testing easy.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an integer guess.

    Returns a tuple ``(ok, value, error)`` where ``ok`` indicates that the
    conversion succeeded, ``value`` is the integer (or ``None`` on failure),
    and ``error`` is an error message suitable for display.
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare ``guess`` to ``secret`` and return ``(outcome, message)``.

    The UI expects two values so we still return both, but the tests generally
    only look at the first element.

    **Bug fix**
    Historically the function attempted to compare mixed types (e.g. an
    integer guess with a string secret) which raised a ``TypeError``.  The
    fallback converted the guess to a string and performed a lexicographic
    comparison, which produced incorrect high/low hints for some numeric
    combinations.  The new logic normalizes both values to integers when
    possible, ensuring numeric comparisons are correct regardless of the
    original types.
    """
    # try to coerce both sides to integers so that the "glitch" (string
    # secret on alternating turns) doesn't confuse the comparison.
    try:
        g_val = int(guess)
        s_val = int(secret)
    except Exception:
        # fall back to original behaviour if coercion fails entirely
        if guess == secret:
            return "Win", "🎉 Correct!"
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

    if g_val == s_val:
        return "Win", "🎉 Correct!"
    if g_val > s_val:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Update and return a new score based on the outcome and attempt.

    This is a pure function distilled from the app; it has no Streamlit
    dependencies so it is easy to test separately.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score

