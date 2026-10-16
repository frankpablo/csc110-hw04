import pytest
import hw04  # Import the module here

# Part 1
# ===========
@pytest.mark.parametrize("word", ["", "a", "lengthy"])
def test_4_1_word_bad_length(capsys, monkeypatch, word):
    # Create a list of input values
    user_inputs = iter([word])
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.my_for_loop()
    captured = capsys.readouterr()
    expected = "bad word"
    assert captured.out == expected + "\n", "Tip: Did you check the length, print `bad word` and return?"
