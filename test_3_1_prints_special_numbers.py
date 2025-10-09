import pytest
import hw04  # Import the module here
import sys

# Part 1
# ===========
def test_3_1_prints_special_numbers(capsys, monkeypatch):
    # Create a list of input values
    # user_inputs = iter(["hello there, I like food"])
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # with monkeypatch.context() as m:
    # m.setattr('builtins.input', lambda _: next(user_inputs))
    hw04.get_special_numbers()
    captured = capsys.readouterr()
    expected = "3\n9\n21\n27\n33\n39"
    assert expected in captured.out, "Tip: Check you ar eprinting one integer per line and only the expected ones."

