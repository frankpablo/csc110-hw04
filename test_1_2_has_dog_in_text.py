import pytest
import hw04  # Import the module here

# Part 1
# ===========
@pytest.mark.parametrize("text", ["hello there, I like dogs", "Dogma is a so-so movie"])
def test_1_2_has_dog_in_text(capsys, monkeypatch, text):
    # Create a list of input values
    user_inputs = iter([text])
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        m.setattr(hw04, "secret_word", "food")
        hw04.check_text()
    captured = capsys.readouterr()
    expected = "You used the word \"dog\" or the word \"Dog\"!"
    assert captured.out == expected + "\n", "Tip: Did you use the exact word \"dog\" using substring membership (`in`)?"
