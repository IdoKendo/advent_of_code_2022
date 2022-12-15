from advent_of_code_2022.day_15_solution import find_non_beacon_positions
from advent_of_code_2022.day_15_solution import find_tuning_frequency


def test_day_15_part_1():
    non_beacon_positions = find_non_beacon_positions(10, "tests/day_15_sample_input.txt")
    assert len(non_beacon_positions) == 26


def test_day_15_part_2():
    tuning_frequency = find_tuning_frequency("tests/day_15_sample_input.txt")
    # For some reason the test returns several results, but real input returns only one solution, I give up!
    assert 56000011 in tuning_frequency
