from advent_of_code_2022.common import read_input


def get_item_value(item: str) -> int:
    if item.islower():
        return ord(item) - 96
    elif item.isupper():
        return ord(item) - 38
    else:
        raise ValueError(f"Received a non-item value: {item}")


def sum_of_priority_items(input_file_path: str) -> int:
    common_items_value = 0
    for line in read_input(input_file_path):
        compartments = line[: len(line) // 2], line[len(line) // 2 :]  # noqa: E203
        common_items = set(compartments[0]).intersection(compartments[1])
        for item in common_items:
            common_items_value += get_item_value(item)
    return common_items_value


def sum_of_elf_groups(input_file_path: str, elf_group_size: int = 3) -> int:
    elf_groups_sum = 0
    groups = zip(*(iter(read_input(input_file_path)),) * elf_group_size)
    for group in groups:
        common_items = set.intersection(*map(set, group))
        for item in common_items:
            elf_groups_sum += get_item_value(item)
    return elf_groups_sum


def main():
    priorities_sum = sum_of_priority_items("input.txt")
    print(priorities_sum)
    elf_groups_sum = sum_of_elf_groups("input.txt")
    print(elf_groups_sum)


if __name__ == "__main__":
    main()
