import pytest
import hw04  # Import the module here
import sys

# Part 1
# ===========
def test_1_3_try_again(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["hello there, no secret word", "second channce works"])
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.secret_word = "works"
        hw04.check_text()
    captured = capsys.readouterr()
    expected1 = "Try again"
    expected2 = "You used the secret word!"
    assert expected1 in captured.out, "Tip: You should not accept a text that has neither the ecret word nor the word \"dog\""
    assert expected2 in captured.out, "Tip: You should have iterated the loop after the message \"Try again\""
