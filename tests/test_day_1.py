from advent_of_code_2022.day_1_solution import create_elves_list
from advent_of_code_2022.day_1_solution import find_most_calories


def test_day_1_star_1():
    list_of_elves = create_elves_list("tests/day_1_sample_input.txt")
    calories_count = find_most_calories(list_of_elves)
    assert calories_count == 24000


def test_day_1_star_2():
    list_of_elves = create_elves_list("tests/day_1_sample_input.txt")
    calories_count = find_most_calories(list_of_elves, 3)
    assert calories_count == 45000
