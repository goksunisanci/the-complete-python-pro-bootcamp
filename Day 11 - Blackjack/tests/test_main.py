import pytest

from src.main import is_player_lose


@pytest.mark.parametrize("case_name,player_cards,computer_cards,expected_value",
                         [
                             ("Player Hand Smaller Case", [1], [2], True),
                             ("Player Hand Bigger Case", [2], [1], False),
                             ("Player Hand Over 21", [22], [1], True),
                         ])
def test_is_player_lose(case_name, player_cards, computer_cards, expected_value):
    lose = is_player_lose(player_cards, computer_cards)
    assert lose == expected_value
