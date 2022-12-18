from advent_of_code_2022.day_18_solution import find_surface_area


def test_day_18_part_1():
    surface_area = find_surface_area("tests/day_18_sample_input.txt")
    assert surface_area == 64


def test_day_18_part_2():
    surface_area = find_surface_area("tests/day_18_sample_input.txt", include_trapped_droplets=False)
    assert surface_area == 58
