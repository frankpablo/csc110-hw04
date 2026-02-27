import pytest
import hw04  # Import the module here
import sys

# Part 1
# ===========
def test_5_2_goodbye_repeat(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["b","b"])
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.my_while_loop()
    captured = capsys.readouterr()
    expected1 = "Goodbye\nChoose one option: a, b, or c: "
    assert expected1 in captured.out, "Tip: if you select `b`, it should print `Goodbye` and repeat the prompt in a new line."
