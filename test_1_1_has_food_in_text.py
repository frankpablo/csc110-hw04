import pytest
import hw04  # Import the module here

# Part 1
# ===========
def test_1_1_has_food_in_text(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["hello there, I like food"])
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        m.setattr(hw04, "secret_word", "food")
        hw04.check_text()
    captured = capsys.readouterr()
    expected = "You used the secret word!"
    assert captured.out == expected + "\n", "Tip: Did you use the exact secret word using substring membership (`in`)?"
