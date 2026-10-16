import pytest
import hw04  # Import the module here

# Part 1
# ===========
def test_5_3_try_again(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["d","b"])
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.my_while_loop()
    captured = capsys.readouterr()
    expected1 = "try again\nGoodbye"
    assert captured.out == expected1 + "\n", "Tip: if you don't select `a`, `b`, or `c`, it should print `try again` and repeat."
