from advent_of_code_2022.day_14_solution import get_time_until_abyss


def test_day_14_part_1():
    time_until_abyss = get_time_until_abyss("tests/day_14_sample_input.txt")
    assert time_until_abyss == 24


def test_day_14_part_2():
    time_until_no_more_sand = get_time_until_abyss("tests/day_14_sample_input.txt", has_floor=True)
    assert time_until_no_more_sand == 93
