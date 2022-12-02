from advent_of_code_2022.day_2_solution import calculate_score
from advent_of_code_2022.day_2_solution import calculate_score_2


def test_day_2_star_1():
    score = calculate_score("tests/day_2_sample_input.txt")
    assert score == 15


def test_day_2_star_2():
    score = calculate_score_2("tests/day_2_sample_input.txt")
    assert score == 12
