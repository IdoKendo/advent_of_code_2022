from advent_of_code_2022.day_8_solution import count_visible_trees
from advent_of_code_2022.day_8_solution import find_highest_score


def test_day_8_part_1():
    num_of_visible_trees = count_visible_trees("tests/day_8_sample_input.txt")
    assert num_of_visible_trees == 21


def test_day_8_part_2():
    highest_score = find_highest_score("tests/day_8_sample_input.txt")
    assert highest_score == 8
