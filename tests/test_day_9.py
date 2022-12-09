from advent_of_code_2022.day_9_solution import count_rope_tail_positions


def test_day_9_part_1():
    positions_tail_visited = count_rope_tail_positions("tests/day_9_sample_input.txt")
    assert positions_tail_visited == 13


def test_day_9_part_2():
    positions_tail_visited = count_rope_tail_positions("tests/day_9_sample_input_part_2.txt", 10)
    assert positions_tail_visited == 36
