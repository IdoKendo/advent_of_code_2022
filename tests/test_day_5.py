from advent_of_code_2022.day_5_solution import move_and_get_top_of_crates


def test_day_5_part_1():
    top_of_crates = move_and_get_top_of_crates("tests/day_5_sample_input.txt")
    assert top_of_crates == "CMZ"


def test_day_5_part_2():
    top_of_crates = move_and_get_top_of_crates("tests/day_5_sample_input.txt", move_at_once=True)
    assert top_of_crates == "MCD"
