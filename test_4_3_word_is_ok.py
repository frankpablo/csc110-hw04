import pytest
import hw04  # Import the module here
import sys

# Part 1
# ===========
def test_4_1_word_is_ok(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["good"])
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.my_for_loop()
    captured = capsys.readouterr()
    expected = "g is a consonant\no is a vowel\no is a vowel\ng is a consonant"
    assert expected in captured.out, "Tip: Did you check vowel vs not vowel; did you print correctly?"
