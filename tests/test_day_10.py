from advent_of_code_2022.day_10_solution import calculate_register_values
from advent_of_code_2022.day_10_solution import get_crt_image
from advent_of_code_2022.day_10_solution import get_sum_of_signals


def test_day_10_part_1():
    register_values = calculate_register_values("tests/day_10_sample_input.txt")
    sum_of_signals = get_sum_of_signals(register_values)
    assert sum_of_signals == 13140


def test_day_10_part_2():
    register_values = calculate_register_values("tests/day_10_sample_input.txt")
    crt_image = get_crt_image(register_values)
    assert crt_image[0] == "##..##..##..##..##..##..##..##..##..##.."
    assert crt_image[1] == "###...###...###...###...###...###...###."
    assert crt_image[2] == "####....####....####....####....####...."
    assert crt_image[3] == "#####.....#####.....#####.....#####....."
    assert crt_image[4] == "######......######......######......####"
    assert crt_image[5] == "#######.......#######.......#######....."
