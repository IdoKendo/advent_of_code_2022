from advent_of_code_2022.day_3_solution import sum_of_elf_groups
from advent_of_code_2022.day_3_solution import sum_of_priority_items


def test_day_3_part_1():
    total_sum = sum_of_priority_items("tests/day_3_sample_input.txt")
    assert total_sum == 157


def test_day_3_part_2():
    total_sum = sum_of_elf_groups("tests/day_3_sample_input.txt")
    assert total_sum == 70
