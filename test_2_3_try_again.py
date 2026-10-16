import pytest
import hw04  # Import the module here

# Part 1
# ===========
def test_2_3_try_again(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["5", "5", "4", "6"])
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.check_greater()
    captured = capsys.readouterr()
    expected1 = "Try again"
    expected2 = "Second is Greater"
    assert captured.out == expected1 + "\n" + expected2 + "\n", "Tip: You should print \"Try again\" if the numbers are equal"
