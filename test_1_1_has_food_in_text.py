import pytest
import hw04  # Import the module here
import sys

# Part 1
# ===========
def test_1_1_has_food_in_text(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["hello there, I like food"])
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.secret_word = "food"
        hw04.check_text()
    captured = capsys.readouterr()
    expected = "You used the secret word!"
    assert expected in captured.out, "Tip: Did you use the exact secret word and compared using ==?"
