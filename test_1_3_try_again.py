import pytest
import hw04  # Import the module here

# Part 1
# ===========
def test_1_3_try_again(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["hello there, no secret word", "second chance works"])
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        m.setattr(hw04, "secret_word", "works")
        hw04.check_text()
    captured = capsys.readouterr()
    expected1 = "Try again"
    expected2 = "You used the secret word!"
    assert captured.out == expected1 + "\n" + expected2 + "\n", "Tip: You should not accept a text that has neither the secret word nor the word \"dog\""
