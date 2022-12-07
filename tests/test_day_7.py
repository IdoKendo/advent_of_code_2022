from advent_of_code_2022.day_7_solution import free_up_space
from advent_of_code_2022.day_7_solution import get_folder_structure
from advent_of_code_2022.day_7_solution import get_total_size


def test_day_7_part_1():
    folder_structure = get_folder_structure("tests/day_7_sample_input.txt")
    assert folder_structure["/a/e"] == 584
    assert folder_structure["/a"] == 94853
    assert folder_structure["/d"] == 24933642
    assert folder_structure["/"] == 48381165
    total_size = get_total_size(folder_structure)
    assert total_size == 95437


def test_day_7_part_2():
    folder_structure = get_folder_structure("tests/day_7_sample_input.txt")
    size_freed_up = free_up_space(folder_structure)
    assert size_freed_up == 24933642
