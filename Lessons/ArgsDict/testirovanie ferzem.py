import pytest
from yandex_testing_lesson import is_under_queen_attack


def test_wrong_type_position():
        with pytest.raises(TypeError):
                is_under_queen_attack(1, "e2")


def test_wrong_value_position():
        with pytest.raises(ValueError):
                is_under_queen_attack("abc", "e2")


def test_wrong_type_queen_position():
        with pytest.raises(TypeError):
                is_under_queen_attack("e2", 1)


def test_wrong_value_queen_position():
        with pytest.raises(ValueError):
                is_under_queen_attack("e2", "abc")


def test_wrong_value():
        with pytest.raises(ValueError):
                is_under_queen_attack("abc", "abc")


def test_wrong_type():
        with pytest.raises(TypeError):
                is_under_queen_attack(1, 1)