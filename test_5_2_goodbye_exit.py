import pytest
import hw04  # Import the module here

# Part 1
# ===========
def test_5_2_goodbye_exit(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["b"])
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.my_while_loop()
    captured = capsys.readouterr()
    expected1 = "Goodbye"
    assert captured.out == expected1 + "\n", "Tip: if you select `b`, it should print `Goodbye` and return"
