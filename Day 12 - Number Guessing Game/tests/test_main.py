import pytest
from src.main import get_turn_by_difficulty, get_answer


@pytest.mark.parametrize("case_name,difficulty,expected_value",
                         [
                             ("Easy Difficulty Case", "easy", 10),
                             ("Hard Difficulty Case", "hard", 5)
                         ])
def test_get_turn_by_difficulty(case_name, difficulty, expected_value):
    turn = get_turn_by_difficulty(difficulty)
    assert turn == expected_value


@pytest.mark.parametrize("case_name,question,user_input,valid_options, expected_value",
                         [
                             ("Validity for Starting Game", "question", "y", ["y", "n"], "y"),
                             ("Validity for not Starting Game", "question", "n", ["y", "n"], "n"),
                             ("Validity for get Easy Difficulty", "question", "easy", ["easy", "hard"], "easy"),
                             ("Validity  for get Hard Difficulty", "question", "hard", ["easy", "hard"], "hard"),
                         ])
def test_get_answer(case_name, question, user_input, valid_options, expected_value, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    value = get_answer(question, valid_options)
    assert value == expected_value
