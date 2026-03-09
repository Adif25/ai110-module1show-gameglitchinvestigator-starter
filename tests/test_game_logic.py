import os
import sys

# make sure the top‑level package is importable when running pytest from the
# project root; many students run the tests directly from within the `tests`
# directory, which otherwise means Python can't find our modules.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_string_secret_comparison():
    # regression test for the bug where the secret was a string and the
    # comparison produced incorrect high/low hints
    outcome, _ = check_guess(60, "50")
    assert outcome == "Too High"
    outcome, _ = check_guess(40, "50")
    assert outcome == "Too Low"
