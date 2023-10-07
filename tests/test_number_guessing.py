from unittest.mock import patch

from number_guessing.number_guessing import check_answer, set_difficulty


def test_set_difficulty_easy():
    with patch("builtins.input", side_effect=["easy"]):
        result = set_difficulty()
        assert result == 10


def test_difficulty_level_hard():
    with patch("builtins.input", side_effect=["hard"]):
        result = set_difficulty()
        assert result == 5


def test_check_answer():
    assert check_answer(50, 55, 6) == 5
    assert check_answer(60, 63, 4) == 3
