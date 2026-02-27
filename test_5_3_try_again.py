import pytest
import hw04  # Import the module here
import sys

# Part 1
# ===========
def test_5_3_try_again(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["d","b"])
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.my_while_loop()
    captured = capsys.readouterr()
    expected1 = "try again"
    assert expected1 in captured.out, "Tip: if you don't select `a`, `b`, or `c`, it should print `try again` and repeat."
