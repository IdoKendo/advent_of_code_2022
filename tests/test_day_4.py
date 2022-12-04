from advent_of_code_2022.day_4_solution import get_any_overlap
from advent_of_code_2022.day_4_solution import get_total_overlap


def test_day_4_part_1():
    num_of_total_overlapping_ranges = get_total_overlap("tests/day_4_sample_input.txt")
    assert num_of_total_overlapping_ranges == 2


def test_day_4_part_2():
    num_of_any_overlapping_ranges = get_any_overlap("tests/day_4_sample_input.txt")
    assert num_of_any_overlapping_ranges == 4
