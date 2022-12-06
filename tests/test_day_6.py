from advent_of_code_2022.day_6_solution import find_marker


def test_day_6_part_1():
    assert find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert find_marker("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_day_6_part_2():
    assert find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert find_marker("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26
