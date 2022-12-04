from collections.abc import Callable

from advent_of_code_2022.common import read_input


def create_set_from_task(task: str) -> set[int]:
    start, end = task.split("-")
    return {i for i in range(int(start), int(end) + 1)}


def get_overlap(input_file_path: str, overlap_condition: Callable[[set, set], bool]) -> int:
    overlap_count = 0
    for line in read_input(input_file_path):
        task1, task2 = line.split(",")
        set1 = create_set_from_task(task1)
        set2 = create_set_from_task(task2)
        if overlap_condition(set1, set2):
            overlap_count += 1
    return overlap_count


def get_total_overlap(input_file_path: str) -> int:
    return get_overlap(input_file_path, overlap_condition=lambda set1, set2: set1.issubset(set2) or set2.issubset(set1))


def get_any_overlap(input_file_path: str) -> int:
    return get_overlap(input_file_path, overlap_condition=lambda set1, set2: set1.intersection(set2))


def main():
    num_of_total_overlapping_ranges = get_total_overlap("input.txt")
    print(num_of_total_overlapping_ranges)
    num_of_any_overlapping_ranges = get_any_overlap("input.txt")
    print(num_of_any_overlapping_ranges)


if __name__ == "__main__":
    main()
