import pytest
from unittest import mock
import hw04  # Import the module here
import sys

# Part 1
# ===========
@mock.patch('builtins.input')
def test_5_1_repeat(mock_input):
    # Create a list of input values
    mock_input.side_effect = ['a', 'b']
    hw04.my_while_loop()
    # Verifies all 2 were called
    assert mock_input.call_count == 2, "Tip: if you select `a`, it should just repeat the prompt in a new line."
