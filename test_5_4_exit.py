import pytest
from unittest.mock import patch
import hw04  # Import the module here
import sys

# Part 1
# ===========
def test_5_4_exit(monkeypatch):
    # Mock the input to return 'q'
    monkeypatch.setattr('builtins.input', lambda _: 'c')

    # Verify sys.exit(1) is raised
    with pytest.raises(SystemExit) as excinfo:
        hw04.my_while_loop()()

    # Assert the specific exit code (1 in this example)
    assert excinfo.value.code is None or excinfo.value.code == 0, "Tip: if you select `c`, it should exit immediately."


    # Create a list of input values
    # user_inputs = iter(["c","b"])
    # # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # with monkeypatch.context() as m:
    #     m.setattr('builtins.input', lambda _: next(user_inputs))
    #     hw04.my_while_loop()
    # captured = capsys.readouterr()
    # expected1 = "Goodbye"
    # expected2 = "The End"
    # assert expected1 not in captured.out, "Tip: if you select `c`, it should exit immediately."
    # assert expected2 not in captured.out, "Tip: if you select `c`, it should exit immediately."
