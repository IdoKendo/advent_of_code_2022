from advent_of_code_2022.day_16_solution import find_most_pressure_released


def test_day_16_part_1():
    most_pressure_released = find_most_pressure_released("tests/day_16_sample_input.txt", time_left=30)
    assert most_pressure_released == 1651


def test_day_16_part_2():
    most_pressure_released = find_most_pressure_released(
        "tests/day_16_sample_input.txt", num_of_workers=2, time_left=26
    )
    assert most_pressure_released == 1707
