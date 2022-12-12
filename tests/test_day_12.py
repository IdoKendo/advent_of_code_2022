from advent_of_code_2022.day_12_solution import find_shortest_path


def test_day_12_part_1():
    steps_taken = find_shortest_path("tests/day_12_sample_input.txt")
    assert steps_taken == 31


def test_day_12_part_2():
    steps_taken = find_shortest_path("tests/day_12_sample_input.txt", starting_elevation="a")
    assert steps_taken == 29
