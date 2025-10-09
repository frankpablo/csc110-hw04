import pytest
import hw04  # Import the module here
import sys

# Part 1
# ===========
def test_1_2_has_dog_in_text(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["hello there, I like dogs"])
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.secret_word = "food"
        hw04.check_text()
    captured = capsys.readouterr()
    expected = "You used the word \"dog\" or the word \"Dog\"!"
    assert expected in captured.out, "Tip: Did you use the exact word \"dog\" and compared using ==?"
