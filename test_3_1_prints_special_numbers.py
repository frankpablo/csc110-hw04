import pytest
import hw04  # Import the module here

# Part 1
# ===========
def test_3_1_prints_special_numbers(capsys, monkeypatch):
    # Create a list of input values
    hw04.get_special_numbers()
    captured = capsys.readouterr()
    expected = "3\n9\n21\n27\n33\n39"
    assert captured.out == expected + "\n", "Tip: Check you are printing one integer per line and only the expected ones."

