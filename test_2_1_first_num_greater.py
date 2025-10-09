import pytest
import hw04  # Import the module here
import sys

# Part 1
# ===========
def test_2_1_first_num_greater(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["5", "1"])
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.check_greater()
    captured = capsys.readouterr()
    expected = "First is Greater"
    assert expected in captured.out, "Tip: check the comparison logic and the spelling of the printout."
