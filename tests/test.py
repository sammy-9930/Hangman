import pytest

from main import validate_game_choice, validate_user_choice

pytestmark = [pytest.mark.unit]


def test_validate_user_choice():
    assert validate_user_choice(1) == True
    assert validate_game_choice(0) == True
    assert validate_user_choice(5) == False


def test_game_choice():
    assert validate_game_choice(2) == True
    assert validate_game_choice(1) == True
    assert validate_game_choice(8) == False
