import pytest
import hw04


def test_5_4_exit(monkeypatch):
    # Selecting c must exit the program rather than return to the caller.
    monkeypatch.setattr("builtins.input", lambda _: "c")
    with pytest.raises(SystemExit):
        hw04.my_while_loop()
