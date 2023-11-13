"""Hello. Your computer has a virus."""
import pytest
from source.nemain import Fighter, Fight


@pytest.fixture(name="coding")
def coding_fixture():
    """
    Doing some shi.
    """
    fighter_1 = Fighter("Tyler Derden", 100, 13)
    fighter_2 = Fighter("Narrator", 100, 13)
    fight = Fight(fighter_1, fighter_2)
    fight.potato()
    yield fight


def test_attack(coding):
    """
    Tests attack.
    """
    coding.fighter_1.attack(coding.fighter_2)
    assert coding.fighter_2.health == 87


def test_get_winner(coding):
    """
    Tests winner.
    """
    assert coding.get_winner() == "Tyler Derden"


def test_heal(coding):
    """
    Tests healing.
    """
    coding.fighter_1.heal(10)
    assert coding.fighter_1.health == 110


def test_potato(coding):
    """
    Tests the potato.
    """
    assert coding.potato() + "is chilling" == "The potato is chilling"


if __name__ == "__main__":
    pytest.main()
