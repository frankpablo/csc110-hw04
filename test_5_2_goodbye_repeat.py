import pytest
import hw04  # Import the module here
import sys

# Part 1
# ===========
def test_5_2_goodbye_exit(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["b"])
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.my_while_loop()
    captured = capsys.readouterr()
    expected1 = "Goodbye"
    assert expected1 in captured.out, "Tip: if you select `b`, it should print `Goodbye` and return"
