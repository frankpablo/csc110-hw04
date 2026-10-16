import pytest
import hw04  # Import the module here

# Part 1
# ===========
@pytest.mark.parametrize("word", ["good", "go", "AEIOU"])
def test_4_3_word_is_ok(capsys, monkeypatch, word):
    # Create a list of input values
    user_inputs = iter([word])
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw04.my_for_loop()
    captured = capsys.readouterr()
    expected = {
        "good": "letter g is a consonant\nletter o is a vowel\nletter o is a vowel\nletter d is a consonant",
        "go": "letter g is a consonant\nletter o is a vowel",
        "AEIOU": "letter A is a vowel\nletter E is a vowel\nletter I is a vowel\nletter O is a vowel\nletter U is a vowel",
    }[word]
    assert captured.out == expected + "\n", "Tip: Did you check vowel vs not vowel; did you print correctly?"
