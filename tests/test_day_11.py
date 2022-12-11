from advent_of_code_2022.day_11_solution import calculate_monkey_business_level


def test_day_11_part_1():
    monkey_business_level = calculate_monkey_business_level("tests/day_11_sample_input.txt")
    assert monkey_business_level == 10605


def test_day_11_part_2():
    monkey_business_level = calculate_monkey_business_level(
        "tests/day_11_sample_input.txt", round_count=10_000, relief_factor=0
    )
    assert monkey_business_level == 2713310158
