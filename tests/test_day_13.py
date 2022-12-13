from advent_of_code_2022.day_13_solution import get_decoder_key
from advent_of_code_2022.day_13_solution import get_right_ordered_packets


def test_day_13_part_1():
    right_ordered_packets = get_right_ordered_packets("tests/day_13_sample_input.txt")
    assert sum(right_ordered_packets) == 13


def test_day_13_part_2():
    decoder_key = get_decoder_key("tests/day_13_sample_input.txt")
    assert decoder_key == 140
