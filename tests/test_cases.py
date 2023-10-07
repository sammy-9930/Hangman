from main import validate_game_choice, validate_user_choice


def test_validate_user_choice():
    assert validate_user_choice(1)
    assert validate_user_choice(0)
    assert not validate_user_choice(5)


def test_game_choice():
    assert validate_game_choice(2)
    assert validate_game_choice(1)
    assert not validate_game_choice(8)
