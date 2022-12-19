from advent_of_code_2022.day_19_solution import calculate_blueprints_quality_level


def test_day_19_part_1():
    blueprints_quality_level = calculate_blueprints_quality_level("./tests/day_19_sample_input.txt", time_limit=24)
    assert blueprints_quality_level == 33


def test_day_19_part_2():
    blueprints_quality_level = calculate_blueprints_quality_level(
        "./tests/day_19_sample_input.txt", time_limit=32, blueprints_count=3
    )
    assert blueprints_quality_level == 3472
