import pytest
import hw04  # Import the module here

# Part 1
# ===========
def test_2_2_second_num_greater(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["1", "5"])
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.check_greater()
    captured = capsys.readouterr()
    expected = "Second is Greater"
    assert captured.out == expected + "\n", "Tip: check the comparison logic and the spelling of the printout."
