import pytest
import hw04  # Import the module here
import sys

# Part 1
# ===========
def test_4_1_word_has_spaces(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["is bad"])
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.my_for_loop()
    captured = capsys.readouterr()
    expected = "bad word"
    assert expected in captured.out, "Tip: Did you check for spaces, print `bad word` and return?"
