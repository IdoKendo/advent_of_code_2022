import pytest
from advent_of_code_2022.day_17_solution import simulate_tower_height


def test_day_17_part_1():
    tower_height = simulate_tower_height("tests/day_17_sample_input.txt", rock_count=2022)
    assert tower_height == 3068


@pytest.mark.skip
def test_day_17_part_2():
    tower_height = simulate_tower_height("tests/day_17_sample_input.txt", rock_count=1_000_000_000_000)
    assert tower_height == 1_514_285_714_288
