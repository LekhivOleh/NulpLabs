"""Hello. Your computer has a virus."""
import pytest
from source.nemain import Fighter, Fight


@pytest.fixture(name="setup")
def coding_fixture():
    """
    Doing some shi.
    """
    fighter_1 = Fighter("Tyler Derden", 100, 13)
    fighter_2 = Fighter("Narrator", 100, 13)
    fight = Fight(fighter_1, fighter_2)
    yield fight


def test_attack():
    """
    Tests attack.
    """
    fighter_1 = Fighter("Tyler Derden", 100, 13)
    fighter_2 = Fighter("Narrator", 100, 13)
    fighter_1.attack(fighter_2)
    assert fighter_2.health == 87


def test_get_winner(setup):
    """
    Tests winner.
    """
    winner = setup.get_winner()
    assert winner == "Tyler Derden"


if __name__ == "__main__":
    pytest.main()
