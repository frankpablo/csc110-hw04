import pytest
import hw04  # Import the module here
import sys

# Part 1
# ===========
def test_5_4_exit(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["c","b"])
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.my_while_loop()
    captured = capsys.readouterr()
    expected1 = "Goodbye"
    expected2 = "The End"
    assert expected1 not in captured.out, "Tip: if you select `c`, it should exit immediately."
    assert expected2 not in captured.out, "Tip: if you select `c`, it should exit immediately."
